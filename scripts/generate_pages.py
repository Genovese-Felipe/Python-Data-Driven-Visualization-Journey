"""Generate browser-friendly datasets from source files without importing Dash."""
from pathlib import Path
import ast,csv,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"pages"
LEVELS=("pillar","area","service","task","sub_task")
COST_SRC=ROOT/"dashboards/v2_construction/V2_script.py"
SMART_PY=ROOT/"dashboards/v3_smart_home/Plan_V3_funcional.py"
SMART_CSV=ROOT/"dashboards/v3_smart_home/data.csv"
def literal(path,variable="data"):
    tree=ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id==variable for t in node.targets):
            return ast.literal_eval(node.value)
    raise ValueError(f"No literal {variable} in {path}")
def smart_records():
    if SMART_CSV.exists():
        with SMART_CSV.open(newline="",encoding="utf-8-sig") as f:
            records=list(csv.DictReader(f))
        numeric=("Installation_Cost","Annual_Energy_Savings","Number_of_Devices","Customer_Satisfaction","Latitude","Longitude")
        for row in records:
            for k in numeric:row[k]=float(row[k])
        return records,SMART_CSV
    data=literal(SMART_PY)
    lens={len(v) for v in data.values()}
    if len(lens)!=1:raise ValueError("Mismatched columns in V3")
    names=list(data)
    return [dict(zip(names,[data[k][i] for k in names])) for i in range(next(iter(lens)))],SMART_PY
def csv_write(path,rows):
    with path.open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
def replace_data(path,var,records):
    s=path.read_text(encoding="utf-8")
    payload=json.dumps(records,separators=(",",":"),ensure_ascii=False).replace("<","\\u003c")
    pattern=r"(<script>const "+var+r"=)(.*?)(;</script>)"
    s,count=re.subn(pattern,lambda m:m.group(1)+payload+m.group(3),s,count=1,flags=re.S)
    if count!=1:raise ValueError(f"Embedded variable {var} not found in {path}")
    path.write_text(s,encoding="utf-8")
def main():
    costs=literal(COST_SRC)
    if len(costs)!=49 or len({tuple(r[k] for k in LEVELS) for r in costs})!=len(costs):
        raise ValueError("V2 data/schema changed; review expected 49 unique leaf items")
    for row in costs:
        if any(not str(row[k]).strip() for k in LEVELS):raise ValueError("Blank hierarchy")
        if row["cost"]<0 or row["budgeted_cost"]<0:raise ValueError("Negative cost")
    smart,smart_src=smart_records()
    if len(smart)!=10:raise ValueError("Smart Home source changed; review before deploy")
    for page in ("v1.html","v2.html"):replace_data(SITE/page,"COSTS",costs)
    replace_data(SITE/"v3.html","SMART",smart)
    csv_write(SITE/"construction_costs.csv",costs)
    csv_write(SITE/"smart_home.csv",smart)
    catalog=json.loads((SITE/"catalog.json").read_text(encoding="utf-8"))
    catalog["source_sha256"]={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (COST_SRC,smart_src)}
    (SITE/"catalog.json").write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("Pages regenerated from source:",len(costs),"construction,",len(smart),"smart records")
if __name__=="__main__":main()
