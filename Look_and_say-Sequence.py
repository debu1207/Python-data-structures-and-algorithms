"""
                             STRING PROCESSING:
LOOK-and-SAY SEQUENCE  (link for explanation: https://en.m.wikipedia.org/wiki/Look-and-say_sequence )
 Problem: Given some integer, n. Determine the nth term in the "look-and-say" sequence.
 Example:
     For n = 4, the 4th term in the sequence is 1211.
"""

def next_num(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[ i+ 1]:
            i += 1
            count +=1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

n = int(input("Enter the number of elements in the sequence: \n"))
s ="1"
for i in range(n):
    s=next_num(s)
    print(s)

