import re
s = "Random <tag>first</tag> some text <tag>second</tag> end"
m = re.search(r"<tag>.*</tag>", s)
if m:
    print("Match (greedy):", m.group())

matches = re.findall(r"<tag>.*?</tag>", s)
for i, m in enumerate(matches, 1):
    print(f"Match {i}:", m)