'''
Write the function reverseWord(word) that returns the word in the reverse order.
'''
def reverseWord(string):
	word_reversed = string[::-1]
	return word_reversed

string = 'Hello'
		
print reverseWord(string)