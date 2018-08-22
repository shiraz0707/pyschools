'''
Write a function calCumulativeSum(numbers) that takes in a list of numbers as argument and 
returns the cumulative sum of the list. That is, the new list where the i element is the 
sum of the first i + 1 elements from the original list. For example, the cumulative sum 
of [1, 2, 3] is [1, 3, 6].
'''

def calCumulativeSum(numbers):
	cumulative_list =[ ]
	cumulative_list.append(numbers[0])
	sum = numbers[0]
		
	for i in range (0,len(numbers)-1):
		sum = sum + numbers[i+1]
		cumulative_list.append(sum) 
	
	return cumulative_list


numbers = [13, 15, 17]   
print calCumulativeSum(numbers)