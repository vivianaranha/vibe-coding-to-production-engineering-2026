def require_text(value,max_len=500):
    if not isinstance(value,str) or not value.strip(): raise ValueError("text required")
    v=value.strip()
    if len(v)>max_len: raise ValueError("too long")
    return v
