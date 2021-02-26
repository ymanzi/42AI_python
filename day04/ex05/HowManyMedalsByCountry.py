import pandas as pd
from FileLoader import FileLoader


def howManyMedalsByCountry(df: pd.DataFrame, country: str) -> dict:
	"""
		takes two arguments:
			a pandas.DataFrame which contains the dataset
			a country name.
		returns a dictionary of dictionaries giving the number and type of medal 
		for each competition where the country team earned medals.
		The keys of the main dictionary are the Olympic games' years.
		In each year's dictionary, the key are 'G', 'S', 'B' 
		corresponding to the type of medals won.
	"""
	my_dic = {}
	data = df[df["Team"]== country]
	for year in data.Year.unique():
		year_data = data[data["Year"] == year].drop_duplicates(subset="Event")
		my_dic[year]={"G":year_data.Medal[year_data["Medal"] == "Gold"].count(),
					"S":year_data.Medal[year_data["Medal"] == "Silver"].count(),
					"B":year_data.Medal[year_data["Medal"] == "Bronze"].count() }
	return my_dic


# loader = FileLoader()
# data = loader.load('../resources/athlete_events.csv')
# print(howManyMedalsByCountry(data, 'France'))
