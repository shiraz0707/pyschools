'''
Write a function echoWord(word) that takes in a word as arguments and returns 
a word that repeats itself based on the number of letter in the word.
'''
def echoWord(word):
	new_word = (word + " ") * len(word)
	return new_word

word = 'skywalker'
print echoWord(word) 
