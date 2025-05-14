import sys
from ft_filter import ft_filter


def filterstring(args):
    """
        filterstring(string: str, n: int)
        returns a list containing words for wich it's length is superior to n.
    """
    try:
        args[1] = int(args[1])
    except Exception as e:
        print(f'AssertionError: the arguments are bad. {e}')
        return
    if (len(args) != 2 or type(args[0]) is not str):
        print("AssertionError: the arguments are bad")
        return
    words = args[0].split(" ")
    checkLen = ft_filter(lambda word: len(word) > args[1], words)
    res = list(checkLen)
    print(res)


if __name__ == "__main__":
    sys.argv.pop(0)
    filterstring(sys.argv)
