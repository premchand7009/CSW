import struct

numbers = [10, 20, 30, 40, 50]

with open("numbers.bin", "wb") as f:
    for num in numbers:
        f.write(struct.pack("i", num))

print("Integers written to binary file successfully.")

read_numbers = []
with open("numbers.bin", "rb") as f:
    while True:
        data = f.read(4)
        if not data:
            break
        read_numbers.append(struct.unpack("i", data)[0])

print("Integers read from file:", read_numbers)
