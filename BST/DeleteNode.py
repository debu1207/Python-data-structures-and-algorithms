# BST  Delete operation
"""

When we delete a node, three possibilites arise.
1. Node to be deleted is the leaf: Simply remove from the tree.
2. Node tobe deleted has only one child: Copy the child to the
   node and delete the child

3. Node to be deleted has two children: Find inorder successor
   of the node. Copy contents of the inorder successor to the node
   and delete the inorder successor. 
   Inorder predecessor can also be used.
"""

# python program to demonstrate delte operation
# in binary search tree

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key 

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end= " ")
		inorder(root.right)

def insert(node,key): 

	if node is None:
		return Node(key)

	if key < node.val:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	return node


def minValueNode(node):
	current = node
	while (current.left is not None):
		current = current.left

	return current

def deleteNode(root, key):
	if root is None:
		return root

	if key<root.val:
		root.left = deleteNode(root.left, key)

	elif (key>root.val):
		root.right = deleteNode(root.right, key)

	else:
		if root.left is None:
			temp = root.right
			root = None 
			return temp

		elif root.right is None:
			temp = root.left
			root = None 
			return temp

		temp = minValueNode(root.right)
		root.val = temp.val
		root.right = deleteNode(root.right, temp.val)
	return root

# driver code

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
 
print("Inorder traversal of the given tree")
inorder(root)
 
print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)
