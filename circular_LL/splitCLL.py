# Split a circular linked list into two halves
# this problem uses tortoise and hare algorithm

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class CircularLL:
	def __init__(self):
		self.head = None

	def push(self, data):
		newnode = Node(data)
		temp = self.head
		newnode.next = self.head

		if self.head is not None:
			while (temp.next != self.head):
				temp = temp.next
			temp.next = newnode

		else:
			newnode.next = newnode
		self.head = newnode

	def printList(self):
		temp = self.head
		if self.head != None:
			while True:
				print(temp.val, end = " ")
				temp = temp.next
				if (temp == self.head):
					break

	# tortoise and hare algorithm
	# Function to split a list into two lists.

	def splitcll(self, head1, head2):
		slow = self.head
		fast = self.head
		if self.head == Node:
			return

		# if there are odd node in the cll then 
		# fast.next becomes head and for even nodes
		# fast.next.next becomes head
		while fast.next != self.head and fast.next.next != self.head:
			fast = fast.next.next
			slow = slow.next

		if fast.next.next == self.head:
			fast = fast.next
		head1.head = self.head

		if self.head.next != self.head:
			head2.head = slow.next

		# make second half cll
		fast.next = slow.next

		# make first half circular
		slow.next = self.head


# initialize lists as empty
head = CircularLL()
head1 = CircularLL()
head2 = CircularLL()

head.push(2)
head.push(7)
head.push(6)
head.push(4)
print(f'original cll: ')

head.printList()

# split the list
head.splitcll(head1, head2)
print(f'\nFirst Cll: ')
head1.printList()

print(f'\nSecond Cll: ')
head2.printList()