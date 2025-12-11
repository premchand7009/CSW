with open("example.txt", "w") as f:
    f.write("Hello Python World!")

with open("example.txt", "r") as f:
    first_part = f.read(10)
    print("First 10 characters:", first_part)

    f.seek(0, 0)
    full_content = f.read()
    print("Full file contents after seek():", full_content)
