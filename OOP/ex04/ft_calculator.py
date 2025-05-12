class calculator:
	def dotproduct(v1: list[float], v2: list[float]) -> None:
		ret = 0
		for i in range(len(v1)):
			ret += (v1[i] * v2[i])
		print("Dot product is:", ret)
	def add_vec(v1: list[float], v2: list[float]) -> None:
		ret = []
		for i in range(len(v1)):
			ret.append(v1[i] + v2[i])
		print("Add Vector is :", ret)
	def sous_vec(v1: list[float], v2: list[float]) -> None:
		ret = []
		for i in range(len(v1)):
			ret.append(v1[i] - v2[i])
		print("Sous Vector is :", ret)
