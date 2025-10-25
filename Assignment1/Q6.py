def encrypt(text):
    reversed_text = text[::-1]
    encrypted = list(reversed_text)
    for i in range(0, len(encrypted) - 1, 2):
        encrypted[i], encrypted[i+1] = encrypted[i+1], encrypted[i]
    
    return ''.join(encrypted)


def decrypt(text):
    decrypted = list(text)
    for i in range(0, len(decrypted) - 1, 2):
        decrypted[i], decrypted[i+1] = decrypted[i+1], decrypted[i]
    original = decrypted[::-1]
    
    return ''.join(original)
user_input = input("Enter a string: ")

encrypted_text = encrypt(user_input)
decrypted_text = decrypt(encrypted_text)

print(f"\nEncrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
