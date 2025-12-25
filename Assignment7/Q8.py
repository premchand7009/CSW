import random
import string

letters = [random.choice(string.ascii_lowercase) for _ in range(100)]

count = {ch: 0 for ch in string.ascii_lowercase}
for ch in letters:
    count[ch] += 1

print("Letter\tCount\tFrequency")
for ch in string.ascii_lowercase:
    frequency = count[ch] / 100
    print(f"{ch}\t{count[ch]}\t{frequency:.2f}")
