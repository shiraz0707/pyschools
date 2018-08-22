'''
Write the function removeVowels(word) that removes all the vowels 
('a', 'e', 'i', 'o', 'u') in a word and returns the remaining letters 
in the word.
'''
def removeVowels(string,vowels):
	string_list = list(string) # convert the string to a list

	for i in range(0,len(string_list)):
		if string_list[i] in vowels:
			string_list[i] = '' # remove the vowel
		
	new_string = ''.join(string_list) # converting a list to a string

	new_string = new_string.replace(" ", "")
	return new_string


string = 'I will always love you'
vowels = 'aeiouAEIOU'
		
print removeVowels(string,vowels)