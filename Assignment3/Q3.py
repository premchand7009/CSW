nums = list(map(int, input("Enter integers separated by spaces: ").split()))

first, second, *rest = nums
print("First number:", first)
print("Second number:", second)
print("Remaining numbers:", rest)

first, second = second, first
print(f"After swapping: First: {first}, Second: {second}")

print("Sum of remaining numbers:", sum(rest))

first, *middle, last = nums
print("Unpacking Example:")
print("First:", first)
print("Middle:", middle)
print("Last:", last)
