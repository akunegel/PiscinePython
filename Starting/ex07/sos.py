import sys


def sos(string: str):
    """
    sos(string: str)
    Takes a string in argument and prints it in morse.
    """
    morse = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ', ': '--..--',
        '.': '.-.-.-',
        '?': '..--..',
        '/': '-..-.',
        '-': '-....-',
        '(': '-.--.',
        ')': '-.--.-',
        ' ': '/'
    }
    string = string.upper()
    encoded = []
    for char in string:
        if char not in morse:
            print("AssertionError: the arguments are bad")
            return
        encoded.append(morse[char])

    print(' '.join(encoded))


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("AssertionError: the arguments are bad")
    else:
        sos(sys.argv[1])
