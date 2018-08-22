'''
Write the function search(word, substring) that takes in a word and 
a substring as arguments and returns the position (0 indexed) of the 
substring if it is found in the word. The function returns -1 if the 
substring is not found.
'''
def searchString(word,substring):
	if word.find(substring) > 1:
		msg = 'Substring exist in word'
	else:
		msg = 'Substring DOESNT exist in word'	
	return msg

word = "bananarama"
substring = "xxxx"

print searchString(word,substring)