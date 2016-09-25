def swap(list, index1, index2):
	list[index1],list[index2] = list[index2],list[index1]
	return list
testlist = [2,16,3,5]
print ("original list: ",testlist)
swap(testlist, 0,1)
assert(testlist == [16,2,3,5])
print ("first and second item swapped: ",testlist)
print("")
def smallest(list):
	smallest = list[0]

	for i in list:
		if i < smallest:
			smallest = i
	return smallest
a = smallest(testlist)
print("smallest number in the list: ",a)
assert(a == 2)
print("")
def sumUp(list):
	sum = 0
	for i in list:
		sum = sum + i
	return sum
b = sumUp(testlist)
print("the numbers in the list added together",b)
assert(b == 26)
print("")
def selectionSort(list):
	for index in range(len(list)-1, 0, -1):
		temp = 0
		for i in range(1, index + 1):
			if list[i] > list[temp]:
				temp = i
		newVar = list[index]
		list[index] = list[temp]
		list[temp] = newVar
			

	return list
testlist2 = [4,3,1,2]
print("a new unsorted list: ", testlist2)
selectionSort(testlist2)

testallsame = [1,1,1,1,1]
selectionSort(testallsame)

print("the list is now sorted by selection.", testlist2)
print("")
def insertionSort(list):
	for i in range(1, len(list)):
		value = list[i]
		position = i
		while position > 0 and list[position-1]>value:
			list[position] = list[position-1]
			position = position-1
		list[position]=value
	return list
testlist3 = [8,19,4,3]

print("a new unsorted list: ",testlist3)
insertionSort(testlist3)
assert(testlist3 == [3,4,8,19])
print("the list is now sorted by insertion: ",testlist3)
print("")
def displayBin(x):
	if x == 0 or x == 1:
		return [x]
	y = [0] * x
	z = 0
	while x:
		y[z] = (x%2)
		x >>= 1
		z = z + 1
	
	return y[::-1]
c = displayBin(3)
assert(c == [0,1,1])
print("3 in Binary should be [1,1].", c)
print("")
def addBin(a,b):
	if len(a) < len(b):
		while len(a) < len(b):
			a.insert(0,0)
			output = [0]*(len(b) + 1)
	elif len(b) < len(a):
		while len(b) < len(a):
			b.insert(0,0)
			output = [0]*(len(a) + 1)
	else:
		output = [0]*(len(a) + 1)
	c = a[::-1]
	d = b[::-1]
	
	carry = 0
	for i in range(len(c)):
		temp = carry + c[i] + d[i]
		output[i] = (temp % 2)
		if temp > 1:
			carry = 1
		else:
			carry = 0
	output[len(output)-1] = carry
	return output[::-1]
assert(addBin([0],[0]) == [0,0])
assert(addBin([0],[1]) == [0,1])
assert(addBin([1],[0]) == [0,1])
assert(addBin([1],[1]) == [1,0])
assert(addBin([1,1,1],[1,0,0,0]) == [0,1,1,1,1])
def addInt(x,y):
	a = displayBin(x)
	b = displayBin(y)

	return addBin(a,b)
d = addInt(0,2)
assert(d == [0,1,0])
print("When 0 [0] and 2 [1,0] are added the result is [0,1,0]: ",d)
print("")
assert(addInt(0,0) == [0,0])
assert(addInt(0,1) == [0,1])
assert(addInt(1,1) == [1,0])

def multBin(x,y):
	a = displayBin(x)
	b = displayBin(y)
	x = 0
	
	for i in range(len(b))[::-1]:
		if b[i] == 1:
			temp = a.copy()
			for j in range(x):
				temp[j] = 0
			a = addBin(a,temp)
		x+=1
	return a[::-1]
f = multBin(1,2)
assert(f == [1,0])
print("When 1 [1] and 2 [1, 0] are multiplied the result is [0,1,0]: ",f)
print("")
def newMult(x,y):
	a = displayBin(x)
	b = displayBin(y)
	result = [0]
	for i in range(y):
		result = addBin(result, a)
	return result
g = newMult(5,3)
assert(g == [0,0,0,0,1,1,1,1])
print("5 [1,0,1] multiplied by 3[1,1] is [0,0,1,1,1,1]: ", g)
print("")
def isSorted(List):
	for i in range ( 1, len(List)):
		assert( List[i-1] <= List[i])

isSorted(testlist2)
isSorted(testallsame)

print("the invariant of the selection and insertion sorts is that every interation starting when i = 1, the [i-1] item in the list is sorted.")
print("")


print("The amount of bits necessary to store a positive value of x is: the floor of log sub 2 of x + 1")
print("")


