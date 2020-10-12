class Node:
	def __init__(self, value):
		self.value = value  
		self.next = None 

	def __str__(self):
		return "Node({})".format(self.value) 

	__repr__ = __str__


class Stack:
	'''
		>>> x=Stack()
		>>> x.pop()
		>>> x.push(2)
		>>> x.push(4)
		>>> x.push(6)
		>>> x
		Top:Node(6)
		Stack:
		6
		4
		2
		>>> x.pop()
		6
		>>> x
		Top:Node(4)
		Stack:
		4
		2
		>>> len(x)
		2
		>>> x.peek()
		4
	'''
	def __init__(self):
		self.top = None
		self.count=0
	
	def __str__(self):
		temp=self.top
		out=[]
		while temp:
			out.append(str(temp.value))
			temp=temp.next
		out='\n'.join(out)
		return ('Top:{}\nStack:\n{}'.format(self.top,out))

	__repr__=__str__

	def isEmpty(self):
		if self.top == None:
			return True
		else:
			return False

		
	def __len__(self): 
		return self.count

	def push(self,value):
		node = Node(value)
		node.next = self.top
		self.top = node
		self.count += 1

	 
	def pop(self):
		if self.isEmpty() == False:
			value = self.top.value
			self.top = self.top.next
			self.count -= 1
			return value

	def peek(self):
		if self.isEmpty() == False:
			return self.top.value
