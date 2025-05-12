import sys

if (len(sys.argv) > 2):
	print ("AssertionError: more than one argument is provided")
	exit(1)
if (len(sys.argv) == 1):
	print ("AssertionError: missing argument")
	exit(1)

try:
	if (int(sys.argv[1]) % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")
except:
	print("AssertionError: argument is not an integer")