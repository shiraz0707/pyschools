'''
A string contains a sequence of characters. Elements within a string 
can be accessed using index that starts from 0. Write the function 
getChar(word, pos) that takes in a word and a number as argument and 
returns the character at that position.
'''
def getCharacter(word,position):
	char_in_position = word[position]	
	return char_in_position

word = "killing me softly"
position = 8

print getCharacter(word,position)