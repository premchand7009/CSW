string = "Python"

with open("fixed.txt", "w") as f:
    f.write(string.ljust(20))

with open("variable.txt", "w") as f:
    f.write(string)

with open("fixed.txt", "r") as f:
    fixed_data = f.read()

with open("variable.txt", "r") as f:
    variable_data = f.read()

print("Fixed length storage:", fixed_data)
print("Variable length storage:", variable_data)
print("Fixed length size:", len(fixed_data), "bytes")
print("Variable length size:", len(variable_data), "bytes")
