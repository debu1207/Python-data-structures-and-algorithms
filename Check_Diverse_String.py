"""
A string is called diverse if it contains consecutive (adjacent) letters of the Latin alphabet and each letter occurs exactly once.
For example, the following strings are diverse: "fced", "xyz", "r" and "dabcef".
The following string are not diverse: "az", "aa", "bad" and "babc". Note that the letters 'a' and 'z' are not adjacent.
Formally, consider positions of all letters in the string in the alphabet.
These positions should form contiguous segment, i.e. they should come one by one without any gaps.
And all letters in the string should be distinct (duplicates are not allowed).
You are given a sequence of strings. For each string, if it is diverse, print "Yes". Otherwise, print "No".
"""
def check_diverse_string(input_str):
    input_str = sorted(input_str)
    D = dict()
    for i in input_str:
        if i in D:
            return "NO"
        else:
            D[i] = ord(i)

    cor_seq = list(range(ord(input_str[0]), ord(input_str[0]) + len(input_str)))
    l = []
    for k,v in D.items():
        l.append(v)

    if l == cor_seq:
        return "YES"
    else:
        return "NO"


n = int(input())
I = []
for i in range(n):
    k=input()
    I.append(k)

for i in range(n):
    print(check_diverse_string(I[i]))

"""
OUTPUT :

8
fced
xyz
r
dabcef
az
aa
bad
babc
YES
YES
YES
YES
NO
NO
NO
NO

"""