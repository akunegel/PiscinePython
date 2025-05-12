from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def plot_life_expectancy(path: str, country: str):
	df = load(path)

	country_row = df[df['country'] == country]
	if country_row.empty:
		print(f"No data found for {country}")
		return

	country_data = country_row.drop(columns='country').transpose()
	country_data.columns = ['Life expectancy']
	country_data.index = country_data.index.astype(int)
	country_data = country_data.loc[(country_data.index >= 1800) & (country_data.index <= 2080)]

	plt.figure(figsize=(10, 6))
	plt.plot(country_data.index, country_data['Life expectancy'], color='steelblue')

	plt.xticks(range(1800, 2081, 20))
	plt.yticks(range(30, 91, 10))

	plt.title(f"{country} Life Expectancy Projections")
	plt.xlabel("Year")
	plt.ylabel("Life expectancy")

	plt.show()

if __name__ == "__main__":
	plot_life_expectancy("life_expectancy_years.csv", 'France')
