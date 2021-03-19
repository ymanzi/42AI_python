from FileLoader import FileLoader
import pandas as pd

def howManyMedals(df: pd.DataFrame, name: str) -> dict:
	dic = {}
	data = df[df["Name"]==name][["Year", "Medal"]]
	filter_gold = (data["Medal"] == "Gold")
	filter_silver = (data["Medal"] == "Silver")
	filter_bronze = (data["Medal"] == "Bronze")
	for year in data.Year.unique():
		dic[year] = {"G": data["Medal"][(data["Year"]==year) & filter_gold].count(),
				"S": data["Medal"][(data["Year"]==year) & filter_silver].count(),
				"B": data["Medal"][(data["Year"]==year) & filter_bronze].count() }
	return dic


loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
print(howManyMedals(data, 'Kjetil Andr Aamodt'))