from random import shuffle
import sys
sys.setrecursionlimit(1000000)

class Node:
	def __init__(self, value, to_strict, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.to_strict = to_strict
	
	def insert(self, value):
		if self.value:
			if self.to_strict(value, self.value):
				if self.left is None:
					self.left = Node(value, self.to_strict)
				else:
					self.left.insert(value)
			elif self.to_strict(self.value, value):
				if self.right is None:
					self.right = Node(value, self.to_strict)
				else:
					self.right.insert(value)
		else:
			self.value = value
	
	def list_elements(self):
		lst = []
		def helper(root):
			if root is None:
				return
			else:
				helper(root.left)
				lst.append(root.value)
				helper(root.right)
		helper(self)
		return lst

def tree_sort(lst, to_strict):
	if len(lst) == 0:
		return lst
	root = Node(lst[0], to_strict)
	for i in range(1, len(lst)):
		root.insert(lst[i])
	
	return root.list_elements()

