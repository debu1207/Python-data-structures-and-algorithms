# stack by using classes

class stack:
	def __init__(self):
		self.arr = []
		self.size = 0

	def push(self, data):
		self.arr.append(data)
		self.size += 1

	def size(self):
		return self.size

	def pop(self):
		print(f'pop operation: ')
		return self.arr.pop()

	def empty(self):
		return self.size == 0

	def top(self):
		return self.arr[-1]

	def printstack(self):
		if self.empty():
			print(f'Stack is empty')
			return
		for i in self.arr:
			print(i, end = " ")

def main():
	s = stack()
	s.push(4)
	s.push(3)
	s.push(7)
	s.push(8)
	s.push(1)
	s.printstack()
	s.pop()
	s.printstack()
	print(f'\n{s.empty()}')
	print(s.top())


main()