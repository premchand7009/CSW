import re
s= "1 set of 23 owls, 999 doves." 
pattern=r"\d{2,}"
m=re.search(pattern,s)
if m:
    print(f'"{m.group()}" found at {m.span()}')