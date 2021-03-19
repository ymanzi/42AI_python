import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class MyPlotLib:
	def __init__(self):
		pass

	def histogram(self, df: pd.DataFrame, features: list):
		df[features].hist()
		plt.show()

	def density(self, df: pd.DataFrame, features: list):
		df[features].plot(kind="density")
		plt.show()

	def pair_plot(self, df: pd.DataFrame, features: list):
		sns.pairplot(df[features], markers=".", height=2, plot_kws=dict(linewidth=0))
		plt.show()

	def box_plot(self, df: pd.DataFrame, features: list):		#
		sns.boxplot(data=df[features])
		plt.show()

# from FileLoader import FileLoader
# loader = FileLoader()
# data = loader.load("../resources/athlete_events.csv")

# tmp = MyPlotLib()

# feat = ["Height", "Weight"]
# tmp.histogram(data, feat)
# tmp.density(data, feat)
# tmp.pair_plot(data, feat)
# tmp.box_plot(data, feat)

			

	