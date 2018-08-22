'''
Write the function getCommonLetters(word1, word2) that takes in two words 
as arguments and returns a new string that contains letters found in both 
string. Ignore repeated letters and sort the result in alphabetical order.
'''
def getCommonLetters(word1,word2):
	word1 = set(word1)
	word2 = set(word2)
	
	
	common_letters = word1.intersection(word2)

	letters = " ".join(sorted(common_letters))
	return letters

word1 = 'acbd'
word2 = 'xycabz'

print getCommonLetters(word1,word2)
