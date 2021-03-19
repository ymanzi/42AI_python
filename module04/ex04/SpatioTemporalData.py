import pandas as pd

class SpatioTemporalData:
	"""
		takes a dataset (pandas.DataFrame) as argument
	"""
	def __init__(self, df: pd.DataFrame):
		self.df = df

	def when(self, location: str) -> list:
		"""
			takes a location as an argument and 
			returns a list containing the years 
			where games were held in the given location.
		"""
		return list(self.df[(self.df["City"] == location)]["Year"].unique())

	def where(self, year: int) -> list:
		"""
			takes a date as an argument and returns the location
			where the Olympics took place in the given year.
		"""
		return list(self.df[(self.df["Year"] == year)]["City"].unique())

from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../resources/athlete_events.csv')

sp = SpatioTemporalData(data)
print(sp.when("Athina"))
print(sp.where(1896))