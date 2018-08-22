def countVowels(word):
	count_vowels = 0
	for l in word:
		if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
			count_vowels = count_vowels + 1
	return count_vowels

word = "bananailoveyou"
print ('Total number of vowels in the word ' + str(countVowels(word)))
