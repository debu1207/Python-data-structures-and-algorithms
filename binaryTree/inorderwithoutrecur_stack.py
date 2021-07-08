class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def newinorder(root):
	current = root
	while current is not None:
		if current.left is None:
			yield current.data
			current = current.right

		else:
			pre = current.left
			while pre.right is not None and pre.right is not current:
				pre = pre.right
				if pre.right is None:
					pre.right = current
					current = current.left
				else:
					pre.right = None 
					yield current.data
					current = current.right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
for v in newinorder(root):
    print(v, end=' ')