with open("sample.txt", "w") as file:
    file.write("Python is great.\n")
    file.write("It makes coding simple.")
with open("sample.txt", "r", encoding="utf-8") as g:
    content = g.readlines()
    print("Number of lines:", len(content))
    g.seek(0, 0)
    words = g.read().split()
    print("Number of words:", len(words))
    g.seek(0, 0)
    characters = g.read()
    print("Number of characters:", len(characters))