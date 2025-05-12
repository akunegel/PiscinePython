from load_csv import load
import matplotlib.pyplot as plt
import re

def convert_population_value(value):
    match = re.match(r'([\d.]+)([kM]?)', value)
    
    number, unit = match.groups()
    number = float(number)
    
    if unit == 'k':
        return number * 1000
    elif unit == 'M':
        return number * 1000000
    else:
        return number

def plot_life_expectancy(path: str, country1: str, country2: str):
    df = load(path)

    country1_row = df[df['country'] == country1]
    country2_row = df[df['country'] == country2]

    if country1_row.empty or country2_row.empty:
        print(f"No data found for at least one country.")
        return

    country_data1 = country1_row.drop(columns='country').transpose()
    country_data2 = country2_row.drop(columns='country').transpose()
    
    country_data1.columns = ['Population']
    country_data2.columns = ['Population']
    country_data1['Population'] = country_data1['Population'].apply(convert_population_value)
    country_data2['Population'] = country_data2['Population'].apply(convert_population_value)
    country_data1.index = country_data1.index.astype(int)
    country_data2.index = country_data2.index.astype(int)
    
    country_data1 = country_data1.loc[(country_data1.index >= 1800) & (country_data1.index <= 2050)]
    country_data2 = country_data2.loc[(country_data2.index >= 1800) & (country_data2.index <= 2050)]

    plt.figure(figsize=(9, 6))
    plt.plot(country_data1.index, country_data1['Population'], color='green', label=country1)
    plt.plot(country_data2.index, country_data2['Population'], color='steelblue', label=country2)

    plt.xticks(range(1800, 2050, 40))
    plt.yticks(range(0, 80000000, 20000000), labels=['0', '20M', '40M', '60M'])
    
    plt.legend()
    plt.title(f"Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.show()


if __name__ == "__main__":
    plot_life_expectancy("population_total.csv", 'France', 'Belgium')
