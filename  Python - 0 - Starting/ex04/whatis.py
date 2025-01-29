import sys

if (len(sys.argv) != 2):
    exit()
nb = sys.argv[1]
if (nb % 2 == 1):
    print("I'm Odd.")
else:
    print("I'm Evem.")
print (nb[1])