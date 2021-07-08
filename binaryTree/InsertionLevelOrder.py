# Insertion in a Binary tree in level order

class Node:
	def __init__(self,data):
		self.key = data
		self.left = None
		self.right = None


def inorder(temp):
	if (not temp):
		return

	inorder(temp.left)
	print(temp.key, end = " ")
	inorder(temp.right)

def insert(temp, key):
	if not temp:
		root = Node(key)
	q = []
	q.append(temp)
	while (len(q)):
		temp = q[0]
		q.pop(0)

		if (not temp.left):
			temp.left = Node(key)
			break

		else:
			q.append(temp.left)

		if (not temp.right):
			temp.right = Node(key)
			break
		else:
			q.append(temp.right)

root = Node(10)
root.left = Node(11)
root.left.left = Node(18)
root.right = Node(15)
root.right.left = Node(20)
root.right.right = Node(12)

print("inorder traversal before insertion: ", end=" ")
inorder(root)

key = 12
insert(root, key)
print(f'\nInorder traversal after insertion:', end = " ")
inorder(root)
