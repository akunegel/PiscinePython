def all_thing_is_obj(object: any) -> int:
	if (type(object) is int):
		print("Type not found")
	elif (type(object) == str):
		print(object, "is in the kitchen :", type(object))
	elif (type(object) == list):
		print("List :", type(object))
	elif (type(object) == tuple):
		print("Tuple :", type(object))
	elif (type(object) == set):
		print("Set :", type(object))
	elif (type(object) == dict):
		print("Dict :", type(object))
	return 42