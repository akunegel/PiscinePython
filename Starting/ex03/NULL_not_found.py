import math

def NULL_not_found(object: any) -> int:
	if (object is None):
		print("Nothing:", object, type(object))
		return 0
	elif (type(object) is float and math.isnan(object)):
		print("Cheese:", object, type(object))
		return 0
	elif (type(object) is bool and object == False):
		print("Fake:", object, type(object))
		return 0
	elif (type(object) is str and object == ''):
		print("Empty:", type(object))
		return 0
	elif (type(object) is int and object == 0):
		print("Zero:", object, type(object))
		return 0
	else:
		print("Type not found")
		return 1