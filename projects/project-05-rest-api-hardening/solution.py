"""Project 05: REST API Hardening."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from vibeprod.readiness import score,missing
def main():
 c={"requirements":True,"tests":True,"security":True,"authz":True,"data":True,"reliability":True,"observability":True,"deployment":True,"rollback":True}
 print({"project":"REST API Hardening","score":score(c),"missing":missing(c)})
if __name__=="__main__":main()
