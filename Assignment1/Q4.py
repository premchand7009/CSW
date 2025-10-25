
def is_palindrome_forloop(s):
    
    s = s.lower()
    
    
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

def is_palindrome_twopointer(s):
    
    cleaned = ""
    for ch in s.lower():
        if ch.isalnum():  
            cleaned += ch
    
    
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

text = input("Enter a string: ")

result1 = is_palindrome_forloop(text)
result2 = is_palindrome_twopointer(text)

print("\n--- Palindrome Check Results ---")
print(f"For-loop Check: {'Palindrome' if result1 else 'Not Palindrome'}")
print(f"Two-pointer Check: {'Palindrome' if result2 else 'Not Palindrome'}")
