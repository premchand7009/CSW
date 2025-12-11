filename = "diary.txt"
try:
    with open(filename, "r") as f:
        print("Contents of diary.txt:")
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please check the name.")
