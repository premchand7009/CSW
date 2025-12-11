import struct

number = 1025

little_endian = struct.pack("<H", number)
big_endian = struct.pack(">H", number)

print("Little Endian:", little_endian)
print("Big Endian:   ", big_endian)
