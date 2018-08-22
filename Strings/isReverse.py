'''
Write the function isReverse(word1, word2) that takes two words as arguments 
and returns True if the second word is the reverse of the first word.
'''
def isReverse(word1, word2):
	
	if (word2 == word1[::-1]):
		return True

word1 = 'hello'
word2 = 'olleh'

		
if isReverse(word1,word2) == True:
	print "word2 is the reverse of word1"
else:
	print "word2 is NOT the reverse of word1"