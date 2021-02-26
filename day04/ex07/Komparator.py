from MyPlotLib import MyPlotLib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Komparator:
	def __init__(self, df: pd.DataFrame):
		self.data = df

	def compare_box_plots(self, categorical_var, numerical_var):
		lst_categorical = self.data[categorical_var].unique()
		my_list = []
		# colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']
		for elem in lst_categorical:
			my_list.append (self.data[(self.data[categorical_var] == elem)][numerical_var])
		x = int(len(my_list) / 2)
		y = int(len(my_list) - x)
		fig, axs = plt.subplots(x, y)
		k = 0
		for i in range(x):
			for j in range(y):
				axs[i, j].boxplot(my_list[k])
				k += 1
		plt.show()

		# for elem in lst_categorical:
		# 	data = self.data[(self.data[categorical_var] == elem)][numerical_var]
		# 	sns.boxplot(data)
		# plt.show()

	def density(self, categorical_var, numerical_var) :
		lst_categorical = self.data[categorical_var].unique()
		for elem in lst_categorical:
			data = self.data[(self.data[categorical_var] == elem)][numerical_var]
			sns.distplot(data, hist=False, kde=True, kde_kws={'linewidth': 3}, label = elem)
		plt.legend(prop={'size': 16}, title=categorical_var)
		plt.show()

	def compare_histograms(self, categorical_var, numerical_var):
		lst_categorical = self.data[categorical_var].unique()
		my_list = []
		colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']
		for elem in lst_categorical:
			my_list.append (list(self.data[(self.data[categorical_var] == elem)][numerical_var].dropna()))
		plt.hist(my_list, stacked=False, color = colors[:len(my_list)], label=lst_categorical, density=True, bins = int(180/15))
		plt.legend()
		plt.xlabel(numerical_var)
		plt.show()




from FileLoader import FileLoader
loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
tmp = Komparator(data)
# tmp.compare_histograms("Sex", "Height")
tmp.compare_box_plots("Sex", "Height")
# tmp.density("Sex", "Height")