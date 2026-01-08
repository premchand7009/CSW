import sys

total = 0

for arg in sys.argv[1:]:
    try:
        total += float(arg)
    except ValueError:
        print(f"Error: Invalid input '{arg}'. Please enter only numbers.")
        sys.exit(1)

print("Sum of numbers:", int(total) if total.is_integer() else total)
