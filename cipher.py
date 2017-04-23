# Vigenere Cipher
# Given a key word, repeats it until it is longer than the message to be encrypted
# Each letter of the message is then shifted forward X times, 
# where X is the position in the alphabet of the corresponding character in the generated key

alph = 'abcdefghijklmnopqrstuvwxyz'
keyword = 'walrus'
msg = 'the attack begins at dawn, so be ready' 


def encode(body, secret):
	shiftIndex = -1 # represents current index of the generated key
	translatedMsg = ''
	generatedKey = ''
	while len(generatedKey) < len(body): # repeats keyword until longer than body
		generatedKey += secret
		
	print 'generatedKey: ' + generatedKey
	
	for i in body:
		shiftIndex += 1
		shiftVal = alph.find(generatedKey[shiftIndex]) # finds number of indicies to move char by stepping thru generatedKey
		translatedMsg += shift(i, shiftVal) # passes char and number of spaces to shift
										    # if generatedKey is 'aaaaaa', shiftVal will always be 0
										    # if generatedKey is 'bbbbbb', shiftVal will always be 1...
	
	print translatedMsg
	return translatedMsg


def decode(body, secret):
	shiftIndex = -1
	translatedMsg = ''
	generatedKey = ''
	while len(generatedKey) < len(body):
		generatedKey += secret
		
	for i in body:

		shiftIndex += 1
		shiftVal = 26 - (alph.find(generatedKey[shiftIndex])) # finds inverse of original shift
		translatedMsg += shift(i, shiftVal) 
	
	print translatedMsg

def shift(char, shiftValue):
	
	#  shiftValue denotes how many indices to move current character
	if char.lower() in alph:

		while shiftValue > 0:
			curIndex = alph.find(char) # finds current position in the alphabet
			shiftValue -= 1
			
			if curIndex < len(alph)-1: # if it's not z...
				char = alph[curIndex+1] # move up one index
			else:
				char = alph[0]
        	
		return char
	
	else:

		return char
