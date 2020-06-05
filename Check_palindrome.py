s = "Was it a cat I saw?"
"""
Checking whether a string is a PALINDROME or not.
Solution uses extra space proportional to size string "s"
"""

def is_palindrome_1(s):
    s = ''.join([i for i in s if i.isalpha()]).replace(" ", "").lower()
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

def is_palindrome_2(s):
    i =0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True

print(is_palindrome_1(s))
print(is_palindrome_2(s))