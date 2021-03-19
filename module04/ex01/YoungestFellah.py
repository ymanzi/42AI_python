import pandas as pd

def youngestFellah(df, year):
	"""
	youngestFellah that takes two arguments:
		a pandas.DataFrame which contains the dataset
		an Olympic year.
	The function returns a dictionary containing the age of the youngest woman and man 
	who took part in the Olympics on that year. 
	The name of the dictionary's keys is up to you, 
	but it must be self-explanatory.
"""
	dic = {}
	
	f_sex_filter = ((df["Sex"] == "F") & (df["Year"] == year))
	m_sex_filter = ((df["Sex"] == "M") & (df["Year"] == year))
	
	dic["youngest-man"] = df.loc[m_sex_filter, "Age"].min()
	dic["youngest-woman"] = df.loc[f_sex_filter, "Age"].min()
	
	return dic