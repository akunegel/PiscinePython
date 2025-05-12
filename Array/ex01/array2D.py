def slice_me(family: list, start: int, end: int) -> list:
	if (type(family) != list or start >= len(family) or end >= len(family)):
		print("Error : out of range.")
		return
	col = len(family)
	row = len(family[0])
	for f in family:
		if len(f) != row:
			print("Error : lists not all of same size.")
			return
	print("My shape is : (", col, ",", row, ")")
	if (start < 0):
		start = len(family) + start
	if (end < 0):
		end = len(family) + end
	print("My new shape is : (", end - start, ",", row, ")")
	ret = []
	for i in range(start, end):
		ret.append(family[i])
	return ret