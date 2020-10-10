class Node:
	def __init__(self, value):
		self.value = value  
		self.next = None 
	
	def __str__(self):
		return "Node({})".format(self.value) 

	__repr__ = __str__
						
						  
class Queue:
	'''
		>>> x=Queue()
		>>> x.isEmpty()
		True
		>>> x.dequeue()
		>>> x.enqueue(1)
		>>> x.enqueue(2)
		>>> x.enqueue(3)
		>>> x.dequeue()
		1
		>>> len(x)
		2
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
		return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

	__repr__=__str__

	def isEmpty(self):
		return self.count==0
		

	def enqueue(self, value):
		new_node = Node(value)
		if self.head==None:
			self.head = new_node
			self.tail=new_node
		else:
			self.tail.next=new_node
			self.tail=new_node
			self.count+=1
		

	def dequeue(self):
		if self.head == None:
			return None
		else:
			to_return = self.head.value
			self.head = self.head.next
			return to_return
		

	def __len__(self):
		return self.count
