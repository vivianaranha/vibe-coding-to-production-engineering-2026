def can(role,action):
    matrix={"viewer":{"read"},"editor":{"read","create","update"},"admin":{"read","create","update","delete","manage"}}
    return action in matrix.get(role,set())
def same_tenant(subject_tenant,resource_tenant,role):
    return role=="platform_admin" or subject_tenant==resource_tenant
