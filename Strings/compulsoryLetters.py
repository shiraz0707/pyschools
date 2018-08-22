'''
Write a function isAllLettersUsed(word, letters) that takes in a word as the 
first argument and returns True if the word contains all the letters found 
in the second argument.
'''

def isAllLettersUsed(word, required):
	letter_found = ' '
	for i in range (len(word)):
		#print word[i]
		#print required 
		if word[i] in required:
			letter_found = True
		else:
			letter_found = False
	return letter_found

		
#word = 'xyz'
#word = 'xayz'
word = 'abc'

required = 'abcdefghijklmnopqrstuvw'

if isAllLettersUsed(word, required) == True:
	print 'The letters in word has a matching entry in required'
else:
	print 'The letters in word DOES NOT have a matching entry in required'

