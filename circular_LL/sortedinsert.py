# sorted insert for circular linked list

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
		if self.head != None:
			while (temp.next != self.head):
				temp = temp.next
			temp.next = newnode

		else:
			newnode.next = newnode
		self.head = newnode

	def printList(self):
		temp = self.head
		print(temp.val)
		temp = temp.next
		while (temp != self.head):
			print(temp.val, end = " ")
			temp = temp.next

	def sortedInsert(self,newnode):
		current = self.head 

		if current is None:
			newnode.next = newnode
			self.head = newnode

		elif (current.val >= newnode.val):
			while current.next != self.head:
				current = current.next
			current.next = newnode
			newnode.next = self.head
			self.head = newnode
		else:
			while current.next != self.head and current.next.val < newnode.val:
				current = current.next

			newnode.next = current.next
			current.next = newnode

	def checkcircular(self):
		temp = self.head
		if self.head == None:
			return False
		temp = temp.next
		while temp.next != self.head:
			temp = temp.next
		if temp.next == self.head:
			return True
		return False

arr = [12, 56, 2, 11, 1, 90]
  
list_size = len(arr)
  
start = CircularLL()
  
# Create linked list from the array arr[]
# Created linked list will be 1->2->11->12->56->90
for i in range(list_size):
    temp = Node(arr[i])
    start.sortedInsert(temp)
print(f'{start.checkcircular()}')
  
start.printList()
