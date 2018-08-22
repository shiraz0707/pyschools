'''
Write a function isTripleDouble(word) that takes in a word as argument 
and returns True if the word contains three consecutive double letters.
'''

def isTripleDouble(word):
	for i in range(0, len(word)-1):
		if word[i] == word[i+1]:
			if word[i+2] == word[i+3]:
				if word[i+4] == word[i+5]:
					triple_double_found = True
					return triple_double_found
				else:
					triple_double_found = False
					return triple_double_found
							
word = 'xyzasasbsbscscsrssst'

if isTripleDouble(word) == True:
	print 'Triple Double Found'
else:
	print 'Triple Double NOT Found'
