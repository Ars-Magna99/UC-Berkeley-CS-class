# 2019-07-15 Binary Tree

#BTree is a subclass of the class Tree we created 
class BTree(Tree):
	empty = Tree(None) #empty tree to fill in a missing left branch

	def __init__(self,label,left = empty,right = empty):
		for b in (left,right):
			assert isinstance(b,BTree) or b is BTree.empty
		Tree.__init__(self,label,[left,right])

	@property
	def left(self):
		return self.branches[0]
	@property
	def right(self):
		return self.branches[1]
	
	def fib_tree(n):
		if n == 0 or n == 1:
			return BTree(n)
		else : 
			left = fib_tree(n-2)
			right = fib_tree(n-1)
			fib_n = left.label+right.label
			return BTree(fib_n,[left,right])
	def contents(t):
		if t is BTree.empty:
			return []
		else:
			return contents(t.left) + [t.label]+contents(t.right)

	def balanced_bst(s):
		"""Construct a binary search Tree from a sorted list s		"""
		if not s:
			return BTree.empty
		else:  
		mid = len(s) // 2
		left = balanced_bst(s[:mid])
		right = balanced_bst(s[mid+1:])
		return BTree(s[mid],left,right)

		def largest(t):
			if t.right is BTree.empty:
					return t.label
			else:
					return largest(t.right)
		def second(t):
			if t.is_leaf():
					return None
			elif t.right is BTree.empty:
					return largest(t.left)
			elif t.right.is_leaf():
					return t.label
			else:
					return second(t.right)
		def contains(s,v):
			if s is BTree.empty:
				return False
			elif  s.root == v:
				return True
			elif s.root < v:
				return contains(s.right,v)
			elif s.root > v:
				return contains(s.left,v)




	