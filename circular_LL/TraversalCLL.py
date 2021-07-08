# Circular Linked List (traversal)

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class CircularLL:
	def __init__(self):
		self.head = None

	def push(self, data):
		ptr1 = Node(data)
		temp = self.head

		ptr1.next = self.head
		# if linked list is not none then set then next of last node
		if self.head is not None:
			while (temp.next != self.head):
				temp = temp.next
			temp.next = ptr1
		else:
			ptr1.next = ptr1 # for first node
		self.head = ptr1

	def printList(self):
		temp = self.head
		if self.head is not None:
			while True:
				print(temp.val)
				temp = temp.next
				if (temp == self.head):
					break

 
# Driver program to test above function
 
# Initialize list as empty
cllist = CircularLL()
 
# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)
 
print("Contents of circular Linked List")
cllist.printList()

