class Error(Exception):
	pass

class Foo:
	def __init__(self, n):
		self.mark = False
		self.n = n
		self.bars = []

	def add(self, bar):
		self.bars.append(bar)

def visit(foos, foo, ret):
	if foo.mark:
		raise Error("cycle is found")
	# printFoos(foos)
	foo.mark = True
	bars = foo.bars
	for bar in bars:
		if bar in foos:
			visit(foos, bar, ret)

	foo.mark = False
	# print foo.n, foo in foos
	foos.remove(foo)
	ret.append(foo)

def topological(foos):
	ret = []
	while foos != []:
		foo = foos[0]
		visit(foos, foo, ret)
	return ret

def printFoos(foos):
	for foo in foos:
		print foo.n, " : ",
		for bar in foo.bars:
			print bar.n, ", ",
		print ''

if __name__ == "__main__":

	dic = {}

	l = ["3 1", "6 1", "4 1", "6 4", "6 3", "4 2", "5 4", "5 2"]
	for s in l:
		# s = raw_input()
		# if s == '': break

		m, n = map(int, s.split())
		if m not in dic: dic[m] = Foo(m)
		if n not in dic: dic[n] = Foo(n)

		bar = dic[m]
		foo = dic[n]
		foo.add(bar)

	foos = dic.values()
	# printFoos(foos)
	printFoos(topological(foos))