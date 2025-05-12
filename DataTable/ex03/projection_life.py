from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def format_k(x, _):
		if x >= 1000:
			return f'{int(x/1000)}k'
		return str(int(x))

def projection_life(path1, path2):
	pib = load(path1)
	life_expectancy = load(path2)

	common_countries = pib.index.intersection(life_expectancy.index)
	gdp_1900 = pib.loc[common_countries, '1900']
	life_1900 = life_expectancy.loc[common_countries, '1900']


	valid = gdp_1900.notna() & life_1900.notna()
	gdp_1900 = gdp_1900[valid]
	life_1900 = life_1900[valid]

	plt.figure(figsize=(10, 6))
	plt.scatter(gdp_1900, life_1900)
	plt.xscale('log')

	plt.gca().xaxis.set_major_formatter(FuncFormatter(format_k))

	plt.xlabel("Gross domestic product")
	plt.ylabel("Life Expectancy")
	plt.title("1900")
	plt.show()


if __name__ == "__main__":
	projection_life("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", "life_expectancy_years.csv")