sentence = input("Enter a sentence: ")
separator = input("Enter a separator: ")

clean_sentence = ""
for char in sentence:
    if char.isalnum() or char.isspace():
        clean_sentence = clean_sentence + char

words = clean_sentence.split()
words.sort(reverse=True)
result = separator.join(words)
print(result)
