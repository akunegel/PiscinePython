import sys
from unicodedata import category

def main():
    """'main' takes
    a single string argument and displays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces"""
    if (len(sys.argv) > 2):
        raise AssertionError("Too many arguments provided.")
    elif (len(sys.argv) == 1):
        arg = input("What is the text to count?\n")
    else:
        arg = sys.argv[1]
    codepoints = range(sys.maxunicode + 1)
    punctuation = {c for i in codepoints if category(c := chr(i)).startswith("P")}
    print ("The text contains", len(arg), "characters:") 
    print (sum(1 for c in arg if c.isupper()), "upper letters")
    print (sum(1 for c in arg if c.islower()), "lower letters")
    print (sum(1 for c in arg if c in punctuation), "punctuation marks")
    print(f"{sum(1 for c in arg if c.isspace())} spaces")
    print (sum(1 for c in arg if c.isdigit()), "digits")
if __name__ == "__main__":
    main()
