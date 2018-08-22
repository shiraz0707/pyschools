'''
Write the function countLetter(word, letter) that takes in 
a word and a letter as arguments and returns the number of occurrence 
of that letter in the word
'''
def countLetter(word,letter):
	total_letters = 0	
	for i in word:
		if i == letter:
			total_letters = total_letters + 1
	return total_letters

def countLetterUsingFunction(word,letter):
	total_letters = 0	
	total_letters = word.count(letter)
	return total_letters


word = "bananabananarama"
letter = "a"
total = countLetter(word,letter)
#total = countLetterUsingFunction(word,letter)

print total