#2019-07-14 CS61A LECTURE 19 Linked List

class Link:
	empty = () #define empty as an attribute 

	def __init__(self,first,rest = empty):
		assert rest is Link.empty or isinstance(rest,Link)
		self.first = first
		self.rest= rest  
	@property
	def second(self):
		return self.rest.first
	
	@second.setter
	def second(self,value):
			self.rest.first = value



class Tree:
	def __init__(self,label,brances = []):
		self.label = label 
		for branch in brances:
			assert isinstance(branch,Tree)
			self.branches = list(branches)

	def fib_tree(n):
		if n == 0 or n == 1:
			return Tree(n)
		else : 
			left = fib_tree(n-2)
			right = fib_tree(n-1)
			fib_n = left.label+right.label
			return Tree(fib_n,[left,right])
	def leaves(tree):
		if tree.is_leaf():
			return [tree.leaf]
		else: 
			s = []
			for b in tree.branches:
				s.extend(leaves(b))
			return s 


