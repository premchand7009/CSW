
sentence = input("Enter a sentence: ")

clean_sentence = ''.join(char for char in sentence if char.isalnum() or char.isspace())

clean_sentence = clean_sentence.lower()

words = clean_sentence.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word in sorted(freq):
    print(f"{word}: {freq[word]}")