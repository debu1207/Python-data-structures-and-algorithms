# inorder tree traversal without recursion

"""
Using stack is the obvious way to traverse tree without recursion.
Below is an algroithm for traversing binary tree using stack.


1. Create an empty stack S.
2. Initialize current node as root
3. Push the current node to S and set current = current->left until current is NULL
4. If current is NULL an stack is not empty then
	a) Pop the top time from stack.
	b) Print the popped item,set current = popped_item->right
	c) Go to step 3
5. if current is NULL an stack is empty then we are done.
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None 
		self.right = None

def inorder(root):
	current = root
	stack = [] # initialize empty stack

	while True:
		if current is not None:
			stack.append(current)
			current = current.left
		elif stack:
			current = stack.pop()
			print(current.data, end = " ")
			# we have visited the node and its left
			# subtree, now its right subtree's turn
			current = current.right

		else:
			break
	print(f' ')

# driver code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)
