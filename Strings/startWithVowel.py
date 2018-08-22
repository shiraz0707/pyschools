'''
Write the function startWithVowel(word) that takes in a word as argument 
and returns a substring that starts with the first vowel found in the word. 
The function returns 'No vowel' if the word does not contain any vowel.
'''
def startWithVowel(word):
	vowels = 'aeiou'
	vowel_found = False

	for i in range(0,len(word)):
		if word[i] in vowels and vowel_found == False:
			new_string = word[i:]
			vowel_found = True
		elif vowel_found == False:
			new_string = 'No Vowel'

	return new_string


word = 'risgoogle'
#word = 'apple'
#word = 'xyz'

print startWithVowel(word)
