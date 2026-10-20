#!/usr/bin/env python3
"""Build a no-CDN Plotly Pages site, CSV/JSON API and deterministic model benchmark.

Source datasets are snapshots, not harmonized across repositories.
Run: python vizlab/build.py build / python vizlab/build.py validate / catalog
"""
from __future__ import annotations
import argparse,csv,hashlib,json,html
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
SOURCES={"v1":("v1_v006.csv","cost",23,3085000),"v2":("v2_construction.csv","cost",23,4730000),"v3":("v3_smart_home.csv","Installation_Cost",10,131500)}
LINKS={
 "journey":"https://github.com/Genovese-Felipe/Python-Data-Driven-Visualization-Journey",
 "predictive":"https://github.com/Genovese-Felipe/Python-Data-Plotly-Predictive-Analytics-Dashboard",
 "handbook":"https://github.com/Genovese-Felipe/PythonDataScienceHandbook",
}
CHAPTERS=[("01","IPython","notebooks/01.00-IPython-Beyond-Normal-Python.ipynb"),
 ("02","NumPy","notebooks/02.00-Introduction-to-NumPy.ipynb"),
 ("03","Pandas","notebooks/03.00-Introduction-to-Pandas.ipynb"),
 ("04","Matplotlib","notebooks/04.00-Introduction-To-Matplotlib.ipynb"),
 ("05","Machine Learning","notebooks/05.00-Machine-Learning.ipynb")]
def dump(path,obj):
 path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=str)+"\n",encoding="utf-8")
def read(k):
 with (ROOT/"data"/SOURCES[k][0]).open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def verify():
 items=[]
 for k,(name,col,count,total) in SOURCES.items():
  rows=read(k)
  observed=sum(float(r[col]) for r in rows)
  if len(rows)!=count or int(round(observed))!=total:raise ValueError(f"{k} fixture mismatch")
  items.append({"id":k,"rows":len(rows),"total":observed,"sha256":hashlib.sha256((ROOT/"data"/name).read_bytes()).hexdigest()})
 if int(sum(float(r["budgeted_cost"]) for r in read("v2")))!=4557000:raise ValueError("v2 budget mismatch")
 return {"ok":True,"source_datasets":items,"data_disclaimer":"Separate educational and synthetic datasets; not financially reconciled"}
STYLE="""*{box-sizing:border-box}body{margin:0;background:#081326;color:#e4f2ff;font:16px/1.55 system-ui,-apple-system,Segoe UI,Arial,sans-serif}main{max-width:1360px;margin:auto;padding:28px}header{border-bottom:1px solid #28445e;padding:12px 0}header a,a{color:#54e7c9}nav a{margin-right:17px}h1{letter-spacing:-.04em;font-size:clamp(29px,4vw,58px);line-height:1.1;margin:24px 0}h2{font-size:24px}p,small{color:#adc3d8}.tag{border:1px solid #284a60;padding:4px 9px;border-radius:30px;font-size:12px;color:#63e7d3}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:15px}.card{background:#11253b;border:1px solid #29455e;padding:18px;border-radius:15px;overflow:hidden}.chart{width:100%;height:460px}.note{background:#273039;border:1px solid #695d41;color:#f9d59a;padding:15px;border-radius:12px;margin:24px 0}footer{margin-top:38px;padding:22px 0;border-top:1px solid #29455e;color:#adc3d8;font-size:13px}a:focus-visible{outline:3px solid orange}@media(max-width:650px){main{padding:16px}.grid{grid-template-columns:1fr}}"""
def page(title,desc,figures,js,source):
 from plotly.io import to_html
 content=[]
 for i,(name,fig) in enumerate(figures):
  fig.update_layout(template="plotly_dark",paper_bgcolor="#11253b",plot_bgcolor="#11253b",font={"color":"#e4f2ff"})
  content.append(f'<article class="card"><h2>{html.escape(name)}</h2>{to_html(fig,full_html=False,include_plotlyjs=False,config={"responsive":True,"displaylogo":False})}</article>')
 nav='<nav><a href="index.html">Home</a><a href="dashboard_v1.html">V1</a><a href="dashboard_v2.html">V2</a><a href="dashboard_v3.html">V3</a><a href="dashboard_v4.html">V4</a><a href="learning_map.html">Learning</a><a href="catalog.json">JSON catalog</a></nav>'
 return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{STYLE}</style><script>{js}</script></head><body><main><header>FGen Analytics Lab <span class="tag">ONE HTML · OFFLINE</span>{nav}</header><h1>{html.escape(title)}</h1><p>{html.escape(desc)}</p><div class="note">Dados ilustrativos; fontes e versões separadas. ML sem validação operacional. <a href="{html.escape(source)}">Consultar origem</a></div><section class="grid">{"".join(content)}</section><footer>Offline: Plotly embutido no arquivo. API JSON versionada no diretório <code>api/</code>. Repositórios de origem: <a href="{LINKS["journey"]}">Journey</a>, <a href="{LINKS["predictive"]}">Predictive</a>, <a href="{LINKS["handbook"]}">Handbook</a>.</footer></main></body></html>'
def build():
 import pandas as pd
 import plotly.express as px
 from plotly.offline import get_plotlyjs
 from source_predictive.data import generate_projects
 from source_predictive.predictive import train_delay_model
 site=ROOT/"site";site.mkdir(parents=True,exist_ok=True)
 guard=verify()
 js=get_plotlyjs()
 v1=pd.DataFrame(read("v1"));v1["cost"]=pd.to_numeric(v1["cost"])
 v2=pd.DataFrame(read("v2"));v2[["cost","budgeted_cost"]]=v2[["cost","budgeted_cost"]].apply(pd.to_numeric)
 v3=pd.DataFrame(read("v3"))
 for col in ["Installation_Cost","Annual_Energy_Savings","Customer_Satisfaction","Latitude","Longitude"]:v3[col]=pd.to_numeric(v3[col])
 v4=generate_projects(rows=240,seed=42)
 fit=train_delay_model(v4,seed=42)
 score={"train":fit.train_rows,"test":fit.test_rows,"mae_days":round(fit.mae_days,3),"r2_test":round(fit.r2,4),"kind":"synthetic holdout demo"}
 configs={
 "dashboard_v1.html":("V1 · Hierarquia de custos","23 tarefas de exemplo, hierarquia do notebook v006.",[("Pilar → área → serviço",px.sunburst(v1,path=["pillar","area","service"],values="cost")),("Custos por pilar",px.bar(v1.groupby("pillar",as_index=False)["cost"].sum(),x="cost",y="pillar",orientation="h"))],LINKS["journey"]),
 "dashboard_v2.html":("V2 · Construction Budget","Realizado USD 4.730.000 vs. orçado USD 4.557.000.",[("Composição hierárquica",px.sunburst(v2,path=["pillar","area","service"],values="cost")),("Real × budget",px.bar(v2.groupby("pillar",as_index=False)[["cost","budgeted_cost"]].sum().melt("pillar"),x="pillar",y="value",color="variable",barmode="group"))],LINKS["journey"]),
 "dashboard_v3.html":("V3 · Smart Home","10 instalações sintéticas; gráficos sem tiles externos.",[("Custo e economia anual",px.scatter(v3,x="Installation_Cost",y="Annual_Energy_Savings",color="Installation_Type",hover_name="City")),("Satisfação por cidade",px.bar(v3,x="City",y="Customer_Satisfaction",color="Installation_Type"))],LINKS["journey"]),
 "dashboard_v4.html":("V4 · Predictive PMO",f'240 projetos sintéticos · Random Forest holdout, MAE {score["mae_days"]} dias e R² {score["r2_test"]}',[("Status do portfólio",px.pie(fit.projects,names="status",hole=.5)),("Atraso previsto por orçamento",px.scatter(fit.projects,x="budget",y="predicted_delay_days",color="predicted_risk",hover_name="project_name"))],LINKS["predictive"]),
 }
 for fn,(title,desc,figures,source) in configs.items():(site/fn).write_text(page(title,desc,figures,js,source),encoding="utf8")
 chapter_html=''.join(f'<li><a href="{LINKS["handbook"]}/blob/master/{path}">{id_}. {name}</a></li>' for id_,name,path in CHAPTERS)
 (site/"learning_map.html").write_text(f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Learning Map</title><style>{STYLE}</style><main><a href="index.html">← Lab</a><h1>Data Science Learning Map</h1><p>Referências de capítulos, sem redistribuição dos notebooks.</p><ol>{chapter_html}</ol></main></html>',encoding="utf8")
 cards=''.join(f'<article class="card"><h2><a href="{fn}">{title}</a></h2><p>{desc}</p></article>' for fn,(title,desc,_,_) in configs.items())
 (site/"index.html").write_text(f'<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FGen Analytics Lab</title><style>{STYLE}</style><main><header>FGen Analytics Lab</header><h1>From data to decisions.</h1><p>Três repositórios · quatro dashboards Plotly offline · mapa de estudos · contratos JSON para agentes.</p><section class="grid">{cards}<article class="card"><h2><a href="learning_map.html">Learning Map</a></h2><p>IPython · NumPy · Pandas · visualização · ML</p></article></section><p><a href="catalog.json">API &amp; dataset catalog</a></p></main></html>',encoding="utf8")
 for id_,df in [("v1",v1),("v2",v2),("v3",v3),("v4",fit.projects)]:dump(site/"api"/f"{id_}.json",df.to_dict("records"))
 dump(site/"api"/"model_metrics.json",score)
 dump(site/"api"/"chapters.json",[{"chapter":id_,"name":name,"notebook":path} for id_,name,path in CHAPTERS])
 manifest={"schema_version":"1.0","datasets":guard["source_datasets"],"model":score,"routes":[*configs,"learning_map.html"],"offline":True,"machine_endpoints":[f"api/{x}.json" for x in ("v1","v2","v3","v4","model_metrics","chapters")],"provenance":LINKS}
 dump(site/"catalog.json",manifest)
 (site/".nojekyll").touch()
 return {"ok":True,"pages":len(configs)+2,"model":score,"source":guard}
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument("action",choices=["build","validate","catalog"]);a=p.parse_args(argv)
 result=build() if a.action=="build" else verify() if a.action=="validate" else {"datasets":list(SOURCES),"sources":LINKS,"ok":True}
 print(json.dumps(result,ensure_ascii=False))
if __name__=="__main__":main()
