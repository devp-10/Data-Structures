#Lab #7
#Due Date: 04/24/2020, 11:59PM
########################################
#                                      
# Name:
# Collaboration Statement:             
#  
########################################

class MaxPriorityQueue:
	'''
		>>> h = MaxPriorityQueue()
		>>> h.insert(10)
		>>> h.insert(5)
		>>> h.heap
		[10, 5]
		>>> h.insert(14)
		>>> h.heap
		[14, 5, 10]
		>>> h.insert(9)
		>>> h.heap
		[14, 9, 10, 5]
		>>> h.insert(2)
		>>> h.heap
		[14, 9, 10, 5, 2]
		>>> h.insert(11)
		>>> h.heap
		[14, 9, 11, 5, 2, 10]
		>>> h.insert(6)
		>>> h.heap
		[14, 9, 11, 5, 2, 10, 6]
		>>> h.parent(2)
		14
		>>> h.leftChild(1)
		9
		>>> h.rightChild(1)
		11
		>>> h.deleteMax()
		14
		>>> h.heap
		[11, 9, 10, 5, 2, 6]
		>>> h.deleteMax()
		11
		>>> h.heap
		[10, 9, 6, 5, 2]
		>>> x = MaxPriorityQueue()
		>>> x.insert(2)
		>>> x.insert(7)
		>>> x.deleteMax()
		7
		>>> x.insert(10)
		>>> x.insert(8)
		>>> x.insert(12)
		>>> x.deleteMax()
		12
		>>> x.insert(5)
		>>> x.insert(18)
		>>> x.heap
		[18, 10, 8, 2, 5]
	'''

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
		'''
		self.heap.append(x)
		for i in self.heap:
			j = self.heap.index(i) + 1
			if isinstance(self.leftChild(j), int)==True:
				if self.leftChild(j) > i:
					swap(self.leftChild(j), i)
			if isinstance(self.rightChild(j), int)==True:
				if self.rightChild(j) > i:
					swap(self.rightChild(j), i)
		'''
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













