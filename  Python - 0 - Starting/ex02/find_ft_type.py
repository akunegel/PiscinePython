def all_thing_is_obj(arg):
    if isinstance(arg, list):
        print(f"List : {type(arg)}")
    elif isinstance(arg, tuple):
        print(f"Tuple : {type(arg)}")
    elif isinstance(arg, set):
        print(f"Set : {type(arg)}")
    elif isinstance(arg, dict):
        print(f"Dict : {type(arg)}")
    elif isinstance(arg, str):
        print(f"{arg} is in the kitchen : {type(arg)}")
    else:
        print("Type not found")
    return 42