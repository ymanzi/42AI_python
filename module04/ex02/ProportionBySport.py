import pandas as pd

def proportionBySport(df: pd.DataFrame, year: int, sport: str, gender: str) -> float:
	request_filter = ((df["Year"] == year) & (df["Sport"] == sport) & (df["Sex"] == gender))
	gender_filter = ((df["Sex"] == gender) & (df["Year"] == year))
	return float( df[request_filter].drop_duplicates(subset=["Name"], keep="first").shape[0]  \
		/ df[gender_filter].drop_duplicates(subset=["Name"], keep="first").shape[0] )