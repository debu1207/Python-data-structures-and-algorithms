"""
You are given a set of n segments on the axis Ox, each segment has integer endpoints between 1 and m inclusive.
Segments may intersect, overlap or even coincide with each other.
Each segment is characterized by two integers li and ri (1≤li≤ri≤m) — coordinates of the left and of the right endpoints.
Consider all integer points between 1 and m inclusive. Your task is to print all such points that don't belong to any segment.
The point x belongs to the segment [l;r] if and only if l ≤ x ≤ r.
"""
l=list(map(int, input().split()))
I = []
for i in range(l[0]):
    k = list(map(int, input().split()))
    I.append(k)

def segment(l):
    return [int(i) for i in range(l[0],l[1]+1)]

def count_absent_point(l,I):
    main = []
    count_absent = 0
    absent_num =[]
    for i in I:
        for j in segment(i):
            main.append(j)
    Set = set(main)
    for i in range(1,l[1]+1):
        if i not in Set:
            count_absent += 1
            absent_num.append(i)
    if count_absent!=0:
        print(count_absent)
        print(' '.join([str(x) for x in absent_num]))
    else:
        print(0)

count_absent_point(l,I)