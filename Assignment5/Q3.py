poem_lines = [
    "Roses are red,",
    "Violets are blue,",
    "Python is fun,",
    "And so are you."
]
with open("poem.txt", "w") as file:
    for line in poem_lines:
        file.write(line + "\n")
        
print("Poem written to file successfully.")
print("Reading back from poem.txt:")
with open("poem.txt", "r") as file:
    for line in file:
        print(line.strip())
