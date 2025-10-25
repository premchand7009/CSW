
paragraph = input("Enter a paragraph: ")


clean_paragraph = " ".join(paragraph.split())


title_paragraph = clean_paragraph.title()


vowels = ['A', 'E', 'I', 'O', 'U']
counts = {v:0 for v in vowels}

for char in title_paragraph:
    upper_char = char.upper()
    if upper_char in vowels:
        counts[upper_char] += 1


print("Processed Text:", title_paragraph)  
print("Vowel Counts:", " ".join(f"{v}:{counts[v]}" for v in vowels))
