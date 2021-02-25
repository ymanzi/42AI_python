#!/usr/bin/python

from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../resources/athlete_events.csv")
# data = loader.load("../../day03/resources/solar_system_census.csv")
# loader.display(data, 12)