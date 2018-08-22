def removeFirstAndLast(numList):
	numList.remove(numList[0])
	numList.remove(numList[-1])
	return numList


import random
numList = random.sample(range(30),8)
print numList
print removeFirstAndLast(numList)


