'''
Write the function capitalizeVowels(word) that 
returns the word with all the vowels capitalized.
'''
def capitalizeVowels(string,vowels):
	string_list = list(string) # convert the string to a list

	for i in range(0,len(string_list)):
		if string_list[i] in vowels:
			string_list[i] = string_list[i].upper() # make the letter to uppercase
		
	new_string = ''.join(string_list) # converting a list to a string

	return new_string


string = 'I will always love you'
vowels = 'aeiouAEIOU'
		
print capitalizeVowels(string,vowels)