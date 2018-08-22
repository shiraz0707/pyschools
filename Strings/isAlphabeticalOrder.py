'''
Write a function isAlphabeticalOrder(word) that takes in a word as argument 
and returns True if the word contains letters that are arranged in alphabetical 
order. For example, the letter 'c' should not appear before the letter 'a'.
'''

def isAlphabeticalOrder(word):
	return word == ''.join(sorted(word))
		
word = 'google'

if isAlphabeticalOrder(word) == True:
	print ('The letters of the word is in alphabetical order')
else:
	print ('The letters of the word is NOT in alphabetical order')