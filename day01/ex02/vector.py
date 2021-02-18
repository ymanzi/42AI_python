#!/goinfre/miniconda3/bin/python

class Vector:
	def __init__(self, values, ra = None):
		""" 
			Vector class that allow to make operation between them 
			self.value
			self.size 
		"""

		if (isinstance(values, int) and isinstance(ra, int)):
			self.values = [ float(elem) for elem in range(values, ra, 1) ]
		elif (isinstance(values, int)):
			self.values = [0.0] * values
		elif (isinstance(values, list)):
			self.values = values
		self.size = len(self.values)		
		
	def __str__(self):
		return ("Vector {}".format(self.values))

	def __add__(self, oth):
		if (isinstance(oth, Vector) and len(self.values) == len(oth.values)):
			return [ a + b for a in self.values for b in oth.values ]


	