import math

def NULL_not_found(arg):
    if arg is None:
        print("Nothing: None", type(arg))
        return 0
    elif (isinstance(arg, float)):
        if (math.isnan(arg)):
            print("Cheese: nan", type(arg))
            return 0
        else:
            print(arg, "Type not Found")
            return 1
    
    elif(isinstance(arg, int)):
        if (arg == 0):
            print("Zero: 0", type(arg))
            return 0
        else:
            print("Type not Found")
            return 1
    
    elif(isinstance(arg, str)):
        if (arg == ""):
            print("Empty:", type(arg))
            return 0
        else:
            print("Type not Found")
            return 1
    
    elif(isinstance(arg, bool)):
        if (arg == False):
            print("Fake: False")
            return 0
        else:
            print("Type not Found")
            return 1
    else:
        print("Type not Found")
        return 1