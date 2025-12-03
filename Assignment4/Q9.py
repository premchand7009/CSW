import re

def find(s):
    pattern = r"([A-Z]).*\d"
    m = re.search(pattern, s)
    if not m:
        return None
    return (m.group(1), m.start(1))

print(find("a B blah 9"))