#!/usr/bin/python

from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")

from YoungestFellah import youngestFellah
print(youngestFellah(data, 2004))