'''
Write a function mirrorText(word1, word2) that takes in 2 words as 
arguments and returns a new word in the following order: word1word2word2word1.
'''
def mirrorText(word1,word2):
	new_word = word1 + ' ' + word2 + ' ' + word2 + ' '+ word1
	return new_word

word1 = 'Thomas'
word2 = 'Muller'

print mirrorText(word1,word2)
