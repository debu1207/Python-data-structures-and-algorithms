"""
You have unlimited number of coins with values 1,2,…,n. You want to select some set of coins having the total value of S.
It is allowed to have multiple coins with the same value in the set. What is the minimum number of coins required to get sum S?
Input
The only line of the input contains two integers n and S (1≤n≤100000, 1≤S≤109)
Output
Print exactly one integer — the minimum number of coins required to obtain sum S.
"""
l = list(map(int, input().split()))
def coins_count(n,s):
    l = list(range(1,n+1))
    if s in l:
        return 1

    i = n
    if (s % i) == 0:
        return (s // i)
    elif (s % i) in l:
        return (s // i) + 1
    else:
        i -= 1
        while i > 0:
            if (s % i) == 0:
                return (s // i)
            elif (s % i) in l:
                return (s // i) + 1
            else:
                i -= 1

print(coins_count(l[0], l[1]))

"""
OUTPUT:

6 16
3
"""