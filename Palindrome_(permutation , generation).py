"""
Given a string. Write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forward and backwards.
A permutation is a rearrangement of letter. The palindrome does not need to limited to just dictionary words.

Also write a function to generate a palindrome from given permutation, not necessarily a dictionary word or phrase.
"""

palin_perm = "Tact coa"
not_palin_perm = "was it a cat i saw"

# Time complexity = O(n)
# Space Complexity = O(n)

def is_palin_perm(input_str):
    input_str = input_str.replace(" ","")
    input_str = input_str.lower()

    d = dict()
    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k,v in d.items():
        if v%2 == 1 and odd_count == 0:
             odd_count += 1
        elif v % 2 == 1 and odd_count > 0:
            return False
    return True

def generate_palin(input_str):
    input_str = input_str.replace(" ","").lower()
    if is_palin_perm(input_str) == False:
        return "Palindrome does not exist for this permutation.\n"

    d= dict()
    for i in input_str:
        if i in d:
            d[i] +=1
        else: d[i] = 1

    palin = ""
    rev_pal = ""
    for k,v in d.items():
        if v % 2==0:
            palin += (v//2)*str(k)
        else:
            palin += str(k)

    for i in range(2, len(palin)+1):
        rev_pal += palin[-i]

    return "Possible palindrome : "+palin + rev_pal

print(is_palin_perm(palin_perm))
print(generate_palin(palin_perm))
print(is_palin_perm(not_palin_perm))
print(generate_palin(not_palin_perm))

"""
OUTPUT:

True
Possible palindrome : tacocat
True
Possible palindrome : waasitctisaaw
"""
