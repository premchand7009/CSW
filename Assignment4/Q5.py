import re
def check(w):
    pattern = r"c[aeiou][^aeiou]"
    return bool(re.fullmatch(pattern, w))
print(check("caa"))
print(check("cat"))
print(check("taa"))
print(check("cay"))