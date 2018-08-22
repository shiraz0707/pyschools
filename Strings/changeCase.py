'''
Write the function changeCase(word) that changes the case 
of all the letters in a word and returns the new word.
'''
def changeCase(word):
	upper_string = word.upper()
	return upper_string 

word = "bananarama"
upper_string = changeCase(word)

print upper_string