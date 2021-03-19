#/goinfre/miniconda3/bin/python
#!/usr/bin/python

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
		else:
			raise TypeError("Wrong Init Variables")
		self.size = len(self.values)		
		
	def __str__(self):
		return ("Vector {}".format(self.values))

	def __repr__(self):
		print(self)

	def __add__(self, oth):
		""" vector + int or vector + vector operation """
		if (isinstance(oth, Vector) and len(self.values) == len(oth.values)):
			return Vector([self.values[i] + oth.values[i] for i in range(0, len(self.values))])
		elif (isinstance(oth, int)):
			return Vector([self.values[i] + oth for i in range(0, len(self.values))])
		else:
			raise TypeError("Wrong variables for addition")
	def __radd__(self, oth):
		""" int + vector operation """
		return self + oth
	def __iadd__(self, oth):
		""" += operation """
		if (isinstance(oth, Vector) and len(self.values) == len(oth.values)):
			self.values = [self.values[i] + oth.values[i] for i in range(0, len(self.values))]
		elif (isinstance(oth, int)):
			self.values = [self.values[i] + oth for i in range(0, len(self.values))]
		else:
			raise TypeError("Wrong variables for addition")
		return self

	def __sub__(self, oth):
		""" vector - int or vector - vector operation """
		if (isinstance(oth, Vector) and len(self.values) == len(oth.values)):
			return Vector([self.values[i] - oth.values[i] for i in range(0, len(self.values))])
		elif (isinstance(oth, int)):
			return Vector([self.values[i] - oth for i in range(0, len(self.values))])
		else:
			raise TypeError("Wrong variables for addition")
	def __rsub__(self, oth):
		""" int - vector operation """
		return self - oth
	
	def __truediv__(self, oth):
		""" vector / int or vector / vector operation """
		if (isinstance(oth, Vector) and len(self.values) == len(oth.values)):
			return Vector([self.values[i] / oth.values[i] for i in range(0, len(self.values))])
		elif (isinstance(oth, int) and oth != 0):
			return Vector([self.values[i] / oth for i in range(0, len(self.values))])
		else:
			raise TypeError("Wrong variables for addition")
	def __rtruediv__(self, oth):
		""" int / vector operation """
		return self / oth
	
	def __mul__(self, oth):
		""" vector * int or vector * vector operation """
		if (isinstance(oth, Vector) and len(self.values) == len(oth.values)):
			return Vector([self.values[i] * oth.values[i] for i in range(0, len(self.values))])
		elif (isinstance(oth, int)):
			return Vector([self.values[i] * oth for i in range(0, len(self.values))])
		else:
			raise TypeError("Wrong variables for addition")
	def __rmull__(self, oth):
		""" int * vector operation """
		return self + oth
	
			


	