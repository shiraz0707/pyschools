'''
Write a function rightJustify(word) that takes in a word as argument and return 
a word with leading spaces so that the last letter of the word is in column 50 of the display.
'''
def rightJustify(word):
	new_word = word.rjust(50, ' ')
	return new_word

word1 = 'skywalker'
word2 = 'google'

print rightJustify(word1) 
print rightJustify(word2) 
