'''
Write a function combineList(List1, List2) that takes in two lists 
and return a list with the contents of both list sorted in ascending order and duplicates 
removed.

example: combine(['a', 'p', 'l'], ['g','o','l'])
    	 result should be ['a', 'g', 'l', 'o', 'p']
    	  
    	 combine([8, 2, 10], [2, 5, 1])
    	 result should be [1, 2, 5, 8, 10]

    	 combine(['a', 1, 'z'], [2, 4, 'y'])
    	 result should be [1, 2, 4, 'a', 'y', 'z']

'''
import random

def combineList(List1,List2):
	combined_set = set(List1) | set(List2)					# Combine two lists
	return list(combined_set)

List1 = random.sample(range(30), 8)
print List1

List2 = random.sample(range(30), 8)
print List2

print combineList(List1,List2)