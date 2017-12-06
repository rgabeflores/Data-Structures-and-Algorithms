
DEBUG = True

class Node:

	def __init__(self, data, left=None, right=None):
		self.data = data
		if not(left is None):
			self.left = left
		else:
			self.left = None
		if not(right is None):
			self.right = right
		else:
			self.right = None

	def insert(self, data):
		if data > self.get_data():
			if not(self.right is None):
				self.right.insert(data)
			else:
				self.set_right(data)
		elif data < self.get_data():
			if not(self.left is None):
				self.left.insert(data)
			else:
				self.set_left(data)
		else:
			return

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def set_left(self, data):
		self.left = Node(data)

	def set_right(self, data):
		self.right = Node(data)

	def print_node(self):
		print(self.data)

	def get_data(self):
		return self.data

class BST:

	def __init__(self, root=None):
		if not(root is None):
			self.root = Node(data=root)
		else:
			self.root = None

	def get_root(self):
		return self.root

	def insert(self, data):
		self.root.insert(data)

	def print_nodes(self, root):
		if not(root.left is None):
			self.print_nodes(root.left)
		root.print_node()
		if not(root.right is None):
			self.print_nodes(root.right)



def main():

	if DEBUG:
		_a = [7,5,9,3,1,10,8,6,2,4]

		bst = BST(_a[0])
		for _ in _a:
			bst.insert(_)

		bst.print_nodes(bst.get_root())
		a = bst.get_root()
		b = a.get_left()
		bL = b.get_left()
		bR = b.get_right()
		c = a.get_right()
		cL = c.get_left()
		cR = c.get_right()
		print(_a)
		print("Root", a.get_data())
		print("Left Child of Root", b.get_data())
		print("Right Child of Root", c.get_data())
		print("Left Child of Left", bL.get_data())
		print("Right Child of Left", bR.get_data())
		print("Left Child of Right", cL.get_data())
		print("Right Child of Right", cR.get_data())

if __name__ == "__main__":
	main()