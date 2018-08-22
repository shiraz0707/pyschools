import random

def addOddNumbersInList(num_list):
	odd_sum = 0
	for num in num_list:
		if num % 2 != 0:
			odd_sum = odd_sum + num
	return odd_sum

num_list = random.sample(range(30), 7)
print num_list

print addOddNumbersInList(num_list)