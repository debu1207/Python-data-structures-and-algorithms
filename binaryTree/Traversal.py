# algorithm Inorder(tree):

"""
1. Traverse teh left subtree, ie, call Inorder(left-subtree)
2. Visit the root.
3. Traverse teh right subtree, i.e, call Inorder(right-subtree)

Poster orde traversal:
1. Traverse the left subtree
2. Travers the right subtree
3. visit the root.

"""

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printInorder(root):
	if root:
		# first recur on left child
		printInorder(root.left)
		# print the data of node
		print(root.val)
		# recur on right child
		printInorder(root.right)

def printPostorder(root):
	if root:
		# First recur on left child
		printPostorder(root.left)
		# then recur on right child
		printPostorder(root.right)
		# print the data of node
		print(root.val)

def printPreorder(root):
	if root:
		print(root.val)
		printPreorder(root.left)
		printPreorder(root.right)


# Driver code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f'Preorder traversal of binray tree : ')
printPreorder(root)

print(f'\nInorder traversal of binary tree: ')
printInorder(root)

print(f'\nPostorder traversal of binary tree: ')
printPostorder(root)