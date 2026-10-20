#!/usr/bin/env python3
"""Deterministic, read-only JSON interface to the static FGen portfolio datasets.

Usage:
  python scripts/agent_cli.py catalog
  python scripts/agent_cli.py summary --dataset construction-v2
  python scripts/agent_cli.py filter --dataset construction-v2 --field pillar --equals Construction
  python scripts/agent_cli.py summary --dataset smart-home-v3
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "construction-v2": ROOT / "site/api/construction-v2.json",
    "smart-home-v3": ROOT / "site/api/smart-home-v3.json",
}

def execute(command, dataset=None, field=None, equals=None):
    if command == "catalog":
        return json.loads((ROOT / "site/api/catalog.json").read_text(encoding="utf-8"))
    if dataset not in FILES:
        raise ValueError("Expected --dataset to be construction-v2 or smart-home-v3")
    source = json.loads(FILES[dataset].read_text(encoding="utf-8"))
    rows = source["records"]
    if command == "filter":
        if field not in ("pillar", "area", "service", "region", "city", "installation_type"):
            raise ValueError("Unsupported filter field")
        if equals is None:
            raise ValueError("--equals is required for filter")
        matched = [x for x in rows if str(x.get(field, "")) == equals]
        return {"dataset":dataset,"field":field,"equals":equals,"count":len(matched),"records":matched,"data_status":source["data_status"]}
    if command == "summary":
        result = {"dataset":dataset,"count":len(rows),"data_status":source["data_status"]}
        if dataset == "construction-v2":
            cost = sum(x["cost"] for x in rows)
            budget = sum(x["budgeted_cost"] for x in rows)
            result.update({"cost_total":cost,"budget_total":budget,"variance":cost-budget,
                           "pillars":sorted(set(x["pillar"] for x in rows)),
                           "currency":source["currency"]})
        else:
            result.update({"installation_cost_total":sum(x["installation_cost"] for x in rows),
                           "annual_savings_total":sum(x["annual_energy_savings"] for x in rows),
                           "regions":sorted(set(x["region"] for x in rows)),
                           "currency":source["currency"]})
        return result
    raise ValueError("Unsupported action")

def main():
    parser = argparse.ArgumentParser(description="Read-only AI adapter over versioned example data")
    parser.add_argument("command",choices=("catalog","summary","filter"))
    parser.add_argument("--dataset",choices=sorted(FILES))
    parser.add_argument("--field",choices=("pillar","area","service","region","city","installation_type"))
    parser.add_argument("--equals")
    args = parser.parse_args()
    result = execute(args.command,args.dataset,args.field,args.equals)
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
