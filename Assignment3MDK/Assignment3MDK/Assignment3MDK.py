class Node:
	def __init__(self,value):
		self.value = value
		self.next = None
		self.previous = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

# Inserts value into a new node 
# after the given node
	def insertAfter(self, node, value):
		newNode = Node(value)
		if node.value == self.tail.value:
			self.tail.next = newNode
			newNode.previous = self.tail
			self.tail = newNode
			self.count += 1
		else:
			node.next.previous = newNode
			newNode.next = node.next
			node.next = newNode
			newNode.previous = node
			self.count += 1
		
    
# Inserts value into a new node
# before the given node
	def insertBefore(self, node, value):
		newNode = Node(value)
		if node.value == self.head.value:
			self.head.previous = newNode
			newNode.next = self.head
			self.head = newNode
			self.count += 1
		else:
			node.previous.next = newNode
			newNode.previous = node.previous
			node.previous = newNode
			newNode.next = node
			self.count += 1
		
    
# Adds the given value as the first
# value in the list
	def addFirst(self, value):
		newNode = Node(value)
		if(self.head == None):
			self.head = newNode
			self.tail = self.head
			self.count += 1
		else:
			newNode.next = self.head
			self.head = newNode
			self.head.next.previous = newNode
			self.count += 1

#Adds the given value as the last
#value in the list
	def addLast(self, value):
		newNode = Node(value)		
		if(self.head == None):
			self.head = newNode
			self.tail = self.head
			self.count += 1
		else:
			self.tail.next = newNode
			newNode.previous = self.tail
			self.tail = self.tail.next
			self.count += 1
			

	def first(self):
		return head

	def last(self):
		return tail

	def find(self, value):
		runner = self.head
		while (runner!=None):
			if runner.value == value:
				return runner.value
			else:
				runner = runner.next
		return None
# Removes the given node
# from the list
	def remove(self, node):
		if node.value == self.head.value:
			node.next = self.head
			node.next.previous = None
			node = None
			self.count -= 1
		elif node.value == self.tail.value:
			node.previous = self.tail
			node.previous.next = None
			node = None
			self.count -= 1
		elif self.count <= 1:
			node = None
		else:
			node.next = node.previous.next
			node.previous = node.next.previous
			node = None

		
  
# Returns the number of items in the list
	def count(self):
		return self.count
			
    
# Allows the user to iterate over
# the values (not the nodes)
	def __iter__(self):
		runner = self.head
		while (runner!=None):
			yield runner.value
			runner = runner.next


	#helper function to see if a list is sorted
def isSorted(dalist):
	sorted = True
	for item in range(1,len(dalist)):
		if dalist[item] < dalist[item-1]:
			sorted = False
	if sorted:
		return True
	else:
		return False

   #helper swap function for quicksort
   #not using python swaps for easier transfer to c#
def swap(dalist,index1,index2):
	temp = dalist[index1]
	dalist[index1] = dalist[index2]
	dalist[index2] = temp

	#the pivot helper function for quicksort
def pivotable(dalist, start, end):
	sortTest = isSorted(dalist[start:end+1])
	if sortTest == False:		
		pivot = start
		wall = 0
		for idx in range(1,len(dalist)):
			if dalist[idx] < dalist[pivot]:
				swap(dalist,idx, wall+1)
				wall +=1
		swap(dalist,pivot,wall)

		pivotable(dalist,0,pivot-1)
		pivotable(dalist,pivot+1,len(dalist))
	else:
		pass
	#quick sort algorithms	
def quickSort(dalist):
	if isSorted(dalist):
		return dalist
	else:
		pivot = dalist[0]
		pivotable(dalist, 0, len(dalist))
		return dalist

	#helper function to avoid copy pasting code for quick sort testing
def quickSortTesting(alist):
	print(alist)
	quickSort(alist)
	assert(isSorted(alist) == True)
	print(alist)
	print("")

	#function for testing quick sorts
def quickSortingTests():
	sortedlist = [1,2,3,4,5,6,7,8,9]
	quickSortTesting(sortedlist)

	reversedlist = [9,8,7,6,5,4,3,2,1]
	quickSortTesting(reversedlist)

	unsortedlist = [19,3,49,16,49,8,72,5,16,81,56]
	quickSortTesting(unsortedlist)

	listofone = [1]
	quickSortTesting(listofone)

	listoftwosorted = [1,2]
	quickSortTesting(listoftwosorted)

	listoftworeversed = [2,1]
	quickSortTesting(listoftworeversed)

#function for checking linked list creation
def linkedListTests():
	linklist = LinkedList()
	#adding to the beginning of an empty list

	LinkedList.addFirst(linklist,3)
	assert(linklist.count == 1)

	#inserting at the beginning of a list
	LinkedList.insertBefore(linklist,Node(3),6)
	assert(linklist.count == 2)

	#inserting at the end of a list
	LinkedList.insertAfter(linklist,Node(3),8)
	assert(linklist.count == 3)

	#removing from the beginning of a list
	LinkedList.remove(linklist,Node(6))
	assert(linklist.count == 2)

	#removing from the end of a list
	LinkedList.remove(linklist,Node(8))
	assert(linklist.count == 1)
	#removing a element from a list of length one

	LinkedList.remove(linklist,Node(3))
	assert(linklist.count == 1)


linkedListTests()
quickSortingTests()