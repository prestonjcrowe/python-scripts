# Pig Latin translator

#str = 'What the fuck did you just fucking say about me, you little bitch?'
str = 'status update spread virally across the social networking site, with many Facebook users mocking the boy with photoshopped images for making boastful claims like having'

vowels = ['a', 'e', 'i', 'o', 'u']

def translateBody(text):
	newStr = ''
	curWord = ''
	for i in text:
		
		if i.isalpha():
			curWord += i
			if i == str[-1]:
				newStr += translateWord(curWord)

		else:
			if len(curWord) > 0:
				newStr += translateWord(curWord)
				curWord = ''
				newStr += i

	print newStr

def translateWord(word):
	if word[0].lower() in vowels:
		word += 'way'
	
	else:
		consonants = ''
		for i in range(len(word)):
			if word[i] in vowels:
				word = word[i:]
				word += consonants
				word += 'ay'
				break
			
			else:
				consonants += word[i]

	return word

str = raw_input('Enter text to be translated: ')
translateBody(str)


