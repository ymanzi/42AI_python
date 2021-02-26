import pandas as pd
import matplotlib.pyplot as plt


class MyPlotLib:
	def __init__(self):
		pass

	def histogram(self, df: pd.DataFrame, features: list):
		df[features].hist()
		plt.show()

	
	


from FileLoader import FileLoader
loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")

tmp = MyPlotLib()

feat = ["Height", "Weight"]
tmp.histogram(data, feat)
			

	