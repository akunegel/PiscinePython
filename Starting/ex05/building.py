import sys


def building(args):
    """
    building takesa single string argument
    and displays the sums of its upper-case characters,
    lower-case characters, punctuation characters, digits and spaces.
    """
    punctuation = "!?:;.,'\"[]()/-_"
    spaces = " \t\v\f\r\n"
    if (len(args) == 1):
        text = input("What is the text to count?\n") + '\n'
    else:
        text = str()
        for i in range(1, len(args)):
            text += args[i]
            if (i < len(args) - 1):
                text += ' '
    print("The text contains", len(text), "characters:")
    cap = 0
    min = 0
    pun = 0
    dig = 0
    spa = 0
    for char in text:
        if (char.isupper()):
            cap += 1
        elif (char.islower()):
            min += 1
        elif (char.isnumeric()):
            dig += 1
        elif (char in spaces):
            spa += 1
        elif (char in punctuation):
            pun += 1
    print(cap, "upper letters")
    print(min, "lower letters")
    print(pun, "punctuation marks")
    print(spa, "spaces")
    print(dig, "digits")


if __name__ == "__main__":
    building(sys.argv)
