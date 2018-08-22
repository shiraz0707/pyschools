'''
Write the function getVowels(word) that takes in a word as an argument 
and returns the vowels ('a', 'e', 'i', 'o', 'u') in that word.

'''

def getVowels(word):
	vowels = ' '
	for l in word:
		if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
			vowels = vowels + ' ' + str(l)
	return vowels

word = "ailoveyou"
print ('The vowels in the word are'+ getVowels(word))
