# Insertion of a key

"""
A new key is always inserted at the leafd. We start searching 
a key from the root until we hit a leaf node. Once a leaf node
is found, the new node is added as a child of the leaf node.
"""

# A class for represening the an individual node in a BST.

class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# function to insert a new node with given key

def insertkey(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insertkey(root.right, key)
		else:
			root.left = insertkey(root.left, key)

	return root

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end = " ")
		inorder(root.right)

#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(50)
r = insertkey(r, 30)
r = insertkey(r, 20)
r = insertkey(r, 40)
r = insertkey(r, 70)
r = insertkey(r, 60)
r = insertkey(r, 80)
 
# Print inoder traversal of the BST
inorder(r)

"""
time complexity: worst case time complexity of search
and insert operatoins is O(h) where h is the height of 
the BST

Interesting facts:
1. Inorder traversal of BST always produces sorted output.
2. We can construct a BST with only Preorder or Postorder 
   or lever order traversal.
"""