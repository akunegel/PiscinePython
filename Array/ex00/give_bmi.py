def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""
		Computes BMI with weight / (height * height) formula.
	"""
	res = []
	for i in range(0, len(height)):
		res.append(weight[i] / (height[i] * height[i]))
	return res

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""
	apply_limit(bmi: list[int | float], limit: int) -> list[bool]
	Takes a list of bmi's and a limit n, returns a list of bools, True if bmi is over limit, False if is under or equal.
	"""
	res = []
	for x in bmi:
		if (x > limit):
			res.append(True)
		else:
			res.append(False)
	return res