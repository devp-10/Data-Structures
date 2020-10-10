class Node:
	def __init__(self, value):
		self.value = value  
		self.next = None 
	
	def __str__(self):
		return "Node({})".format(self.value) 

	__repr__ = __str__
												  
class SortedLinkedList:
	'''
		>>> x=SortedLinkedList()
		>>> x.pop()
		>>> x.add(8.76)
		>>> x.add(1)
		>>> x.add(1)
		>>> x.add(1)
		>>> x.add(5)
		>>> x.add(3)
		>>> x.pop()
		8.76
		>>> x.add(-7.5)
		>>> x.add(4)
		>>> x.add(9.78)
		>>> x.add(4)
		>>> x
		Head:Node(-7.5)
		Tail:Node(9.78)
		List:-7.5 1 1 1 3 4 4 5 9.78
	'''

	def __init__(self):   
		self.head=None
		self.tail=None
		self.count=0

	def __str__(self):  
		temp=self.head
		out=[]
		while temp:
			out.append(str(temp.value))
			temp=temp.next
		out=' '.join(out) 
		return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

	__repr__=__str__

	def isEmpty(self):
		return True if self.head==None else False

	def __len__(self):
		return self.count
				
	def add(self, value):
		current = self.head
		previous = None
		while current != None:
			if current.value > value:
				break
			previous = current
			current = current.next
		temp = Node(value)
		if previous == None:
			temp.next, self.head = self.head, temp
		else:
			temp.next, previous.next = current, temp
		self.count = self.count + 1
		current = self.head
		while current.next != None:
			current = current.next
		self.tail = current

	def pop(self):
		if self.isEmpty():
			return
		temp = self.head
		if temp == self.tail:
			self.head = None
			self.tail = None
			self.count = 0
			return temp.value
		while temp.next != self.tail:
			temp = temp.next
		temp.next = None
		tempVal = self.tail.value
		self.tail = temp
		self.count = self.count - 1
		return tempVal

	
	def replicate(self):
		if self.count < 2:
			return
		current = self.head
		while current!=None and current.next!=None:
			if current.value == current.next.value:
				current.next = current.next.next
				return
			else:
				current = current.next
				return
