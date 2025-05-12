import sys

morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def sos(string: str):
	"""
	sos(string: str)
	Takes a string in argument and prints it in morse.
	"""
	for char in string:
		if (char.isalnum() == False):
			print("AssertionError: the arguments are bad")
			return
	string = string.upper()
	encoded = str()
	for char in string:
		encoded += morse.get(char)
		if (char != string[-1]):
			encoded += ' '
	print(encoded)

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("AssertionError: the arguments are bad")
	else:
		sos(sys.argv[1])