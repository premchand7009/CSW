x, y, z = input("Enter three numbers separated by spaces: ").split()
x, y, z = int(x), int(y), int(z)

print(f"Before swapping: x = {x}, y = {y}, z = {z}")
y, z = z, y
print(f"After swapping: x = {x}, y = {y}, z = {z}")
