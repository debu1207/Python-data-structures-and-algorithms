# Implementation using singly linked list

# function: getSize(), isEmpty(), peek(), push(val), pop()

class Node:
	def __init__(self,val):
		self.val = val
		self.next= None

class stack:
	def __init__(self):
		self.head = None 
		self.size = 0

	def push(self, data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode
		self.size += 1

	def __str__(self):
		cur = self.head
		out = ""
		while cur:
			out += str(cur.val) + "->"
			cur = cur.next
		return out

	def getSize(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def peek(self):
		return self.head.val

	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head
		self.head = self.head.next
		self.size -= 1
		return remove.val

stack = stack()
for i in range(1, 11):
    stack.push(i)
print(f"Stack: {stack}")
 
for _ in range(1, 6):
    remove = stack.pop()
    print(f"Pop: {remove}")

print(f"Stack: {stack}")
print(f'Stack size: {stack.getSize()}')
