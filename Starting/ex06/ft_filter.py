def filterstring(fun, arg):
	"""
		filter(function, args: list)
		returns a list of every item in list for wich function(item) returns True.
	"""
	filtered = []
	for x in arg:
		if (fun(x)):
			filtered.append(x)
	return iter(filtered)