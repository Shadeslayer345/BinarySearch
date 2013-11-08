import time, sys, os

numList = [0,26,40,100,0,0,0,0,30,12,1,4,4,5,7,15,8,98,7,84,841,864,1,196,41,654,1684,15641,96,481,361687,564,84641,9841,48]
numList2 = [1254,100,1000000,1,974487,98555,9687,78,4586]
userList = []
Lists = {
	1 : numList,
	2 : numList2,
	3 : userList,
} 
listIndex = 0
'''Code To Either Select A List'''
print "Hello, we are going to sort and search a list"
decisionTime = raw_input("Firstly, would you like to use a list I've generated?(Y/N) ======> ")
'''User Has Choosen To Populate Their Own List'''
if decisionTime == ("N" or "n"):
	listIndex = 3
	print "Okey Dokey, well now lets setup your list"
	numOfList = int(input("Enter the number of integers you want in the List ======> "))
	for x in xrange(numOfList):
		i = int(input("Enter a number to add to the list(Make sure your numbers are random and not sorted =======> "))
		userList.append(i)
		time.sleep(1)
		print "Adding %d to the list" %i
		time.sleep(1)
		print "Added %d to the list" %i

	'''User Has Choosen To Use A Prepopulated and Randomized List'''
elif decisionTime == ("Y" or "y"):
	print "Ok, well I have two lists for you... one short one, one long"
	listIndex = int(input("Which list would you like to use (1 or 2) ======>"))
	print Lists[listIndex]

	#User Has Entered Unsupported Variable
else:
	print "HAHAHA Very Funny, please enter a specified variable(upper or lowercase)"

whatYouWant = int(input("And Finally, enter what value you want to search for..... =======> "))

'''Function To Sort The List'''
#An off-shoot of the Bubble Sort but more efficient in my opinion
#Instead of the traditional double-nested for loop we will utilize a condition for the while loop
def smartBubbleSort(l):
	sorted = False
	print "\nBubble Sorting List......."
	while not sorted:
		sorted = True
		for x in xrange(len(l)-1,0,-1): 
			if l[x] < l[x-1]:
				temp = l[x]
				l[x]  = l[x-1]
				l[x-1] = temp
				sorted = False
	print "\nList sorted........"
	print l

'''Function To Search The Sorted List'''

def binarySearch(l, s):
	smartBubbleSort(l)
	print "\nBinary Searching........."
	found = False
	startSearchParameter = 0
	endSearchParameter = len(l) - 1
	searchValue = s
	while ((not found) and (startSearchParameter <= endSearchParameter)):
		middleValue = ((startSearchParameter+endSearchParameter)/2)
		if searchValue == l[middleValue]:
			found = True
			return "\nSearch value found at position %d" %middleValue
		else:	
			if searchValue < l[middleValue]:
				endSearchParameter = middleValue - 1
			else:
				startSearchParameter = middleValue + 1
	if not found:
		return "Search Value not found.... %d does not appear to be in the given list" %searchValue

binarySearch(numList2, whatYouWant)