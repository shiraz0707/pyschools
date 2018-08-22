'''
Write a function (list1, list2) that takes in two lists as arguments and 
return a list that is the result of removing elements from list1 that can be found in list2.

Examples

subtractList
    subtractList([1,2,3,4,5], [2, 4])
    will result [1, 3, 5]
    
    subtractList (['a', 'b', 'c', 'd'], ['x', 'y', 'z', 'c'])
    will result ['a','b','d']
'''

def subtractList(list1,list2):
	for n in range (0, len(list2)):
		if n not in list2:
			list2.pop()
	return list2

list2 = [1,2]
list1 = [1,2,3,4]

print subtractList(list1, list2)

