'''
Write a function splitWord(word, numOfChar) that takes in a word and a 
number as arguments. The function will split the word into smaller segments 
with each segment containing the number of letter specified in the numOfChar 
argument. These segments are stored and returned in a list.'''

def splitWord(word, numOfChar):
	word_list = [ ]
	i = 0
	while i < len(word):
		word_list.append(word[i:i+(numOfChar)])
		i = i + numOfChar
	return word_list

word = 'abcdefghijklmno'
numOfChar = 3

print splitWord(word, numOfChar)
