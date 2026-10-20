"""Read-only agent interface regression tests; no external libraries required."""
import importlib.util
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class TestAgentCLI(unittest.TestCase):
    def invoke(self,*args):
        p=subprocess.run([sys.executable,str(ROOT/"scripts/agent_cli.py"),*args],
                         capture_output=True,text=True,check=True)
        return json.loads(p.stdout)

    def test_construction_totals(self):
        d=self.invoke("summary","--dataset","construction-v2")
        self.assertEqual(d["count"],49)
        self.assertEqual(d["cost_total"],3085000)
        self.assertEqual(d["budget_total"],2988000)
        self.assertEqual(d["variance"],97000)

    def test_smart_home_rows(self):
        d=self.invoke("summary","--dataset","smart-home-v3")
        self.assertEqual(d["count"],10)
        self.assertIn("annual_savings_total",d)

    def test_filter(self):
        d=self.invoke("filter","--dataset","construction-v2","--field","pillar","--equals","Construction")
        self.assertEqual(d["count"],19)

    def test_catalog_status(self):
        d=self.invoke("catalog")
        self.assertIn("datasets",d)
        self.assertIn("illustrative",d["data_quality"])

if __name__=="__main__":
    unittest.main()
