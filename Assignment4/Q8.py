import re

def extract_date_parts(s):
    pattern=r"(\d\d)-(\d\d)-(\d\d\d\d)"
    m=re.search(pattern,s)
    if not m:
        return None
     
    return (m.group(0),m.group(1),m.group(2),m.group(3),m.span(),m.lastindex)

s= "Backup 05-11-2025 complete"
t= extract_date_parts(s)
print(t)