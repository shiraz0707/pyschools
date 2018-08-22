'''
Write the function countA(word) that takes in a word as argument and 
returns the number of 'a' in that word.
'''
def countA(word):
	totalAs = 0	
	for i in word:
		if i == "a":
			totalAs = totalAs + 1
	return totalAs

def countAUsingFunction(word):
	totalAs = word.count('a')
	return totalAs

word = "bananarama"
#total = countA(word)
total = countAUsingFunction(word)
print total