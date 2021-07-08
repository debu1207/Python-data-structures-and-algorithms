# Write a function to get Nth node in a linked list

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode

	def printList(self):
		temp = self.head
		while temp:
			print(temp.val, end= " ")
			temp = temp.next

	def lengthLL(self):
		if self.head == None:
			return 0
		temp = self.head
		count = 0
		while temp:
			count += 1
			temp = temp.next

		return count

	def nthnode(self, llist, n):
		llist.getNthNode(self.head, n-1, llist)

	def getNthNode(self, head, pos, llist):
		count = 0
		if head:
			if count == pos:
				print(head.val)
			else:
				llist.getNthNode(head.next, pos-1, llist)
		else:
			print('Index Doesn\'t exist')


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(4)
    llist.push(9)
    llist.push(12)
    llist.push(1)
    # llist.getNth(llist,int(input()))
    # Enter the node position here
    # first argument is instance of LinkedList
 
    print("Element at Index 3 is", end=" ")
    llist.nthnode(llist, 3)

