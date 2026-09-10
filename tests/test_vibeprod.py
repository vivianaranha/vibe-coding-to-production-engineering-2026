import sys,unittest
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from vibeprod.readiness import score,missing
from vibeprod.authz import can,same_tenant
from vibeprod.validation import require_text
from vibeprod.idempotency import Store
from vibeprod.quality import release_gate
from vibeprod.ai import MockAI,valid_structured
from vibeprod.metrics import error_rate,availability
class T(unittest.TestCase):
 def test_readiness(self): self.assertEqual(score({x:True for x in ["requirements","tests","security","authz","data","reliability","observability","deployment","rollback"]}),100)
 def test_authz(self): self.assertTrue(can("admin","delete"));self.assertFalse(same_tenant("a","b","editor"))
 def test_validation(self): self.assertEqual(require_text(" x "),"x")
 def test_idempotency(self):
  s=Store();self.assertEqual(s.run("k",lambda:1),(1,False));self.assertEqual(s.run("k",lambda:2),(1,True))
 def test_gate(self): self.assertFalse(release_gate(True,True,True,False)["pass"])
 def test_ai(self): self.assertTrue(valid_structured(MockAI().generate("x"),["text","provider"]))
 def test_metrics(self): self.assertEqual(error_rate(1,10),.1);self.assertEqual(availability(99,100),.99)
if __name__=="__main__":unittest.main()
