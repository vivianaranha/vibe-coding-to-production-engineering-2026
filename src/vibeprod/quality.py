def release_gate(tests,security,review,rollback):
    checks={"tests":tests,"security":security,"review":review,"rollback":rollback}
    return {"pass":all(checks.values()),"failed":[k for k,v in checks.items() if not v]}
