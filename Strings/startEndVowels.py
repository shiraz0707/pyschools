'''
Write the function startEndVowels(word) that 
returns True if the word starts and ends with vowels.
'''
def startEndVowels(string):
	vowels = "aeiouAEIOU" 
	if string[0] in vowels and string[-1:] in vowels:
		return True
	else:
		return False

string = 'adoiy'
print startEndVowels(string)
