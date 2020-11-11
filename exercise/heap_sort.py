class Error(Exception):
	pass

class Heap:
	def __init__(self, *args):
		self.__list = []
		self.__func = lambda x, y : x > y
		params = list(args)
		try:
			if hasattr(args[0], "__call__"):
				self.__func = params.pop(0)
		except Exception:
			pass
		finally:
			self.__list = params

		self.__build_heap()

	def __parent(self, i):
		return (i-1) / 2

	def __left(self, i):
		return (i*2) + 1

	def __right(self, i):
		return (i*2) + 2

	def __heapify(self, i, size):
		H = self.__list
		l = self.__left(i)
		r = self.__right(i)
		# print "__heapify is called: " + str(H) + " and index: " + str(i)+" "+str(l)+" "+str(r)
		try:
			if l < size and self.__func(H[l], H[i]):
				largest = l
			else:
				largest = i

			if r < size and self.__func(H[r], H[largest]):
				largest = r
		except Exception, Error:
			raise Error(str(H[i])+", "+str(H[l])+", "+str(H[r])+" are not comparable.")
		else:
			if largest != i:
				H[i], H[largest] = H[largest], H[i]
				self.__heapify(largest, size)

	def __build_heap(self):
		H = self.__list
		# print "__build_heap is called for: " + str(H)
		for i in range(self.__parent(len(H)-1), -1, -1):
			# print "call heapipy: " + str(i)
			self.__heapify(i, len(H))

	def insert(self, *args):
		H = self.__list
		for e in args:
			H.append(e)
			i = len(H)-1
			p = self.__parent(i)
			while(p >= 0):
				if self.__func(H[i], H[p]):
					H[i], H[p] = H[p], H[i]
					i = p
					p = self.__parent(i)
				else:
					break

	def pop(self):
		H = self.__list
		if len(l) <:
			raise Error("heap underflow")
		m = H[0]
		H[0] = H[-1]
		self.__heapify(0, len(H))


	def sort(self):
		H = self.__list
		size = len(H)
		for i in range(len(H)-1, 0, -1):
			H[0], H[i] = H[i], H[0]
			size -= 1
			heap.__heapify(0, size)
		return H

	@staticmethod
	def heap_sort(*args):
		tmp_heap = Heap(*args)
		# print "    heap has been constucted"
		return tmp_heap.sort()



if __name__=="__main__":
	# list_ = []
	# n = 0
	# while(1):
	# 	try:
	# 		n = input()
	# 		list_.append(n)
	# 	except Exception:
	# 		break

	heap = Heap(9,2,3,1,23,4,0)
	heap.insert(100)
	print heap.sort()
	print Heap.heap_sort(lambda x, y: x < y, 4,5,3,2,5,4,3,0,-1)

	print "end"
