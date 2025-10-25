decimal_num = int(input("Enter a decimal number: "))

binary_str = bin(decimal_num)[2:]
octal_str = oct(decimal_num)[2:]
hex_str = hex(decimal_num)[2:].upper()

print("\n--- Converted Values ---")
print(f"Binary: {binary_str} (Digits: {len(binary_str)})")
print(f"Octal: {octal_str} (Digits: {len(octal_str)})")
print(f"Hexadecimal: {hex_str} (Digits: {len(hex_str)})")

decimal_from_binary = int(binary_str, 2)
decimal_from_octal = int(octal_str, 8)
decimal_from_hex = int(hex_str, 16)

print("\n--- Reconverted to Decimal ---")
print(f"From Binary: {decimal_from_binary}")
print(f"From Octal: {decimal_from_octal}")
print(f"From Hexadecimal: {decimal_from_hex}")