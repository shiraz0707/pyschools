'''
def getMaxNumber(numList):
	max_number = numList[0]
	for num in numList:
		if num > max_number:
			max_number = num
	return max_number
'''

def getMaxNumber(numList):
	return max(numList)





import random
numList = random.sample(range(30),8)
print numList
print getMaxNumber(numList)


