# tuples in loop
from operator import eq
tup = ('geeks', )
n = 5
for i in range(n):
	tup = (tup,)
	print(tup)

# using cmp(), max(), min()
#def cmp(a, b):
#	return (a>b) - (a<b)

tuple1 = ('python', 'geek')
tuple2 = ('coder', 1)

if (eq(tuple1, tuple2) != 0):
	print(f'Not the same')
else:
	print('same')

print(f'Maximum elemen in tuples1,2: {str(max(tuple1))} , {str(max(tuple2))}')
