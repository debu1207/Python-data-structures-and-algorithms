"""
 Given two strings. Write a method to decide if one is a permutation of the other.
"""

perm_1 = input("Enter a word: \n")
perm_2 = input("Enter another word: \n")

# Using Hashtables
def check_perm(str1,str2):
    str1 =str1.lower()
    str2 =str2.lower()
    if len(str1) != len(str2):
        return False

    d1, d2 = dict(),dict()
    for i in str1:
        if i in d1:
            d1[i]+=1
        else: d1[i] = 1

    for i in str2:
        if i in d2:
            d2[i]+=1
        else: d2[i] = 1

    for k,v in d1.items():
        if k in d2:
            if d2[k] != v or k not in d2:
                return False
        else:
            return False
    return True

# Without using hashtables
def check_perm_2(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False

    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    if str1 != str2:
        return False
    else:
        return True

print(check_perm(perm_1,perm_2))
print(check_perm(perm_1,perm_2))

"""
OUTPUT:

Enter a word: 
cat
Enter another word: 
act
True
True
"""
