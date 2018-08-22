
'''
def getMinNumber(numList):
	min_number = numList[0]
	for num in numList:
		if num < min_number:
			min_number = num
	return min_number
'''


def getMinNumber(numList):
	return min(numList)

import random
numList = random.sample(range(30),8)
print numList
print getMinNumber(numList)


