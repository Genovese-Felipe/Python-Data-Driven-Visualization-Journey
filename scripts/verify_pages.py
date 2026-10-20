"""Validate static Pages datasets without importing Dash."""
import csv,json,math
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"pages"
def read(n):
    with (p/n).open(encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f))
def main():
    c,s=read("construction_costs.csv"),read("smart_home.csv")
    assert len(c)==49 and len(s)==10
    assert abs(sum(float(r["cost"]) for r in c)-3085000)<.01
    assert abs(sum(float(r["budgeted_cost"]) for r in c)-2988000)<.01
    assert len({tuple(r[k] for k in ("pillar","area","service","task","sub_task")) for r in c})==49
    for r in c:
        assert all(r[k].strip() for k in ("pillar","area","service","task","sub_task"))
        assert all(math.isfinite(float(r[k])) and float(r[k])>=0 for k in ("cost","budgeted_cost"))
    catalog=json.loads((p/"catalog.json").read_text(encoding="utf-8"))
    assert catalog["data_type"]=="synthetic"
    assert sorted(x["id"] for x in catalog["dashboards"])==["v1","v2","v3"]
    for x in ("v1","v2","v3"):
        html=(p/(x+".html")).read_text()
        assert "assets/plotly.min.js" in html and "assets/app.js" in html
    assert (p/"index.html").exists()
    print("PASS: 49 cost leaves; 10 smart records; reconciled totals.")
if __name__=="__main__":main()
