AREAS=["requirements","tests","security","authz","data","reliability","observability","deployment","rollback"]
def score(checks):
    passed=sum(bool(checks.get(x)) for x in AREAS)
    return round(passed/len(AREAS)*100,1)
def missing(checks):
    return [x for x in AREAS if not checks.get(x)]
