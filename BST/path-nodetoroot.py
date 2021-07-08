# Print path from root to a given node in a binary tree

class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end = " ")
		inorder(root.right)


def insertkey(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val < key:
			return insertkey(root.right, key)

		else:
			return insertkey(root.left, key)

	return root

def pathtonode(root, key):
	if root is None:
		print(f'BST is empty')
		return
	else:
		temp = root
		while temp.val != key:
			if temp.val < key:
				print(temp.val)
				temp = temp.right
			else:
				print(temp.val)
				temp = temp.left
		print(key)


# Driver code
 
r = Node(50)
r = insertkey(r, 30)
r = insertkey(r, 20)
r = insertkey(r, 40)
r = insertkey(r, 70)
r = insertkey(r, 60)
r = insertkey(r, 80)
 
# Print inoder traversal of the BST
inorder(r)

pathtonode(r, 70)


