#!/usr/bin/python

class GotCharacter:
	def __init__(self, first_name = None, is_alive = True):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	""" My first child class (Representing the Stark Family, herited from GotCharacter class """
	def __init__(self, first_name = None, is_alive = True):
		GotCharacter.__init__(self, first_name, is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def __str__(self):
		return "I am {name} from the {family} family and {word}".format(
			name = first_name, family = family_name, word = house_words )
	
	def print_house_words(self):
		print("My Family's Moto is {}".format(self.house_words))
	
	def die(self):
		self.is_alive = False