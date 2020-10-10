class MaxPriorityQueue:
	
	def __init__(self):
		self.heap=[]

	def __str__(self):
		return f'{self.heap}'

	__repr__=__str__

	def __len__(self):
		return len(self.heap)
		

	def parent(self,index):
		if index <= 1 or index > len(self):
			return None
		else:
			return self.heap[index//2 - 1] 
		

	def leftChild(self,index):
		if index < 1 or (2*index) > len(self):
			return None
		else:
			return self.heap[2*index - 1]


	def rightChild(self,index):
		if index < 1 or (2*index + 1) > len(self):
			return None
		else:
			return self.heap[2*index]
	
	
	def insert(self,x):
		self.heap.append(x)
		current = len(self)
		while self.parent(current)!=None and self.parent(current)<x:
			a, b = self.heap.index(self.heap[current-1]), self.heap.index(self.heap[current//2-1])
			self.heap[b], self.heap[a] = self.heap[a], self.heap[b] 
			current = current//2

	def deleteMax(self):
		if len(self)==0:
			return None        
		elif len(self)==1:
			outMax=self.heap[0]
			self.heap=[]
			return outMax

		
		deleted = self.heap[0]
		self.heap.remove(deleted)
		current = 1
		a = self.heap[len(self.heap)-1]
		self.heap.insert(0, a)
		self.heap.pop()
		temp = self.heap[0]
		while self.leftChild(current)!=None:
			if self.rightChild(current)!=None:
				l=self.leftChild(current)
				r=self.rightChild(current)
				maxx = max(l, r)
				if maxx <= temp:
					break
				else:
					if maxx==r:
						a, b = self.heap.index(self.heap[current-1]), self.heap.index(self.heap[current*2])
						self.heap[b], self.heap[a] = self.heap[a], self.heap[b]
					if maxx==l:
						a, b = self.heap.index(self.heap[current-1]), self.heap.index(self.heap[current*2 - 1])
						self.heap[b], self.heap[a] = self.heap[a], self.heap[b]
					current = 2*current + 1
			else:
				if self.leftChild(current)<=temp:
					break
				else:
					a, b = self.heap.index(self.heap[current-1]), self.heap.index(self.heap[current*2 - 1])
					self.heap[b], self.heap[a] = self.heap[a], self.heap[b]
					current=current*2
		return deleted



def heapSort(numList):
	'''
	   >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
	   [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
	'''
	sortHeap = MaxPriorityQueue()
	if type(numList)==list:
		for elements in numList:
			sortHeap.insert(elements)

		final = []
		while len(sortHeap.heap)!=0:
			final.insert(0, sortHeap.heap[0])
			sortHeap.deleteMax()
		return final
	else:
		return None
