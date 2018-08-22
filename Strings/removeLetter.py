'''
Write a function removeLetter(word, letter) that takes in a word and 
a letter as arguments and remove all the occurrence of that particular 
letter from the word. The function will return the remaining leters 
in the word.
'''
def removeLetterUsingFunction(word,letter):
	new_string = word.replace(letter, "")
	return new_string 

def removeLetter(word,letter):	
	word = list(word)
	for i in range (0,len(word)):
		if word[i] == letter:
			word[i]=''
	new_string = ''.join(word)		
	return new_string


word = "bananarama"
letter = "a"
#new_string = removeLetterUsingFunction(word,letter)
new_string = removeLetter(word,letter)

print new_string