##2019-07-16 Objects example
class worker:
	greeting = 'Sir'
	def __init__(self):
		self.elf = Worker
	def work(self):
		return self.greeting + ',I work'
	def __repr__(self):
		return Bourgeoisie.greeting 

class Bourgeoisie(Worker):
	greeting = 'Peon'
	def work(self):
		print(Worker.work(self))
		return 'I gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

#morse code
abcde = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.'}
def morse(code):
	root = Tree(None)
	for letter, signals in sorted(code.items()):
		tree = root
		for signal in signals:
			match = [b for b in tree.branches if b.entry == signal]
			if match:
				assert len(match) == 1
				tree = match[0]
			else:
				branch = Tree(signal)
				tree.branches.append(branch)
				tree = branche
		tree.branches.append(Tree(letter))
	return root  

def decode(signals, tree):
	for signal in signals:
		tree = [b for b in tree.branches if b.entry == signal][0]
	leaves = [b for b in tree.branches if not b.branches]
	assert len(leaves) == 1
	return leaves[0].entry
