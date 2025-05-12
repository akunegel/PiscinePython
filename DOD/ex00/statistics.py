def ft_statistics(*args: any, **kwargs: any) -> None:
	nbs = []
	for arg in args:
		nbs.append(arg)
	
	filters = []
	for value in kwargs.values():
		if value in ["mean", "std", "var", "median", "quartile"]:
			filters.append(value)
	
	for filter in filters:
		if (len(nbs) == 0):
			print("ERROR")
		else:
			if (filter == "mean"):
				mean = sum(nbs) / len(nbs)
				print(f"mean : {mean}")
			elif (filter == "std"):
				mean = sum(nbs) / len(nbs)
				std = 0
				for nb in nbs:
					std += (nb - mean) ** 2
				std = (std / len(nbs)) ** 0.5
				print(f"std : {std}")
			elif (filter == "var"):
				mean = sum(nbs) / len(nbs)
				var = 0
				for nb in nbs:
					var += (nb - mean) ** 2
				var = var / len(nbs)
				print(f"var : {var}")
			elif (filter == "median"):
				nbs.sort()
				if (len(nbs) % 2 == 0):
					median = (nbs[len(nbs) // 2] + nbs[len(nbs) // 2 - 1]) / 2
					print(f"median : {median}")
				else:
					median = nbs[len(nbs) // 2]
					print(f"median : {median}")
			elif (filter == "quartil"):
				nbs.sort()
				q1 = nbs[len(nbs) // 4]
				q3 = nbs[len(nbs) * 3 // 4]
				print(f"quartile : [{q1}, {q3}]")