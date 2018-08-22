def isPalindrome(word):
	return word == word[::-1]
		
word = 'city'

if isPalindrome(word) == True:
	print ('The word ' + word + ' is a palindrome')
else:
	print ('The word ' + word + ' is NOT palindrome')