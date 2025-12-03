import re
pattern=r"^[a-z]+[0-9]+$"
tests = ["abc123", "a1b2", "ABC123", "hello2025", "x9", "x", "123"]

for s in tests:
    if re.fullmatch(pattern, s):
        print(s, "→ pass")
    else:
        print(s, "→ fail")