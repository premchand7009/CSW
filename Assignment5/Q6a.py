filename = "diary.txt"

try:
    with open(filename, "r") as f:
        print("File already exists. Avoiding overwrite.")
except FileNotFoundError:
    note = input("Enter your diary note: ")
    with open(filename, "w") as f:
        f.write(note + "\n")
    print("Diary note saved successfully.")
