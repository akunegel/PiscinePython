import sys

def filterstring(args):
	"""
		filterstring(string: str, n: int)
		returns a list containing words for wich it's length is superior to n.
	"""
	try:
		args[1] = int(args[1])
	except:
		print("AssertionError: the arguments are bad")
		return
	if (len(args) != 2 or type(args[0]) != str):
		print("AssertionError: the arguments are bad")
		return
	words = args[0].split(" ")
	checkLen = lambda word : len(word) > args[1]
	res = [word for word in words if checkLen(word)]
	print(res)



if __name__ == "__main__":
	sys.argv.pop(0)
	filterstring(sys.argv)