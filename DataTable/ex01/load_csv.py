import pandas as pd

def load(path: str):
	try:
		df = pd.read_csv(path)
		print("Loading dataset of dimensions", df.shape)
		return df
	except:
		print("Error reading file.")
		return
	