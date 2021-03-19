#/goinfre/miniconda3/bin/python
#!/usr/bin/python

class Test:
	def __init__(self, matrix):
		# if (isinstance(matrix, tuple)
		# 		# and isinstance(shape, None)
		# 		and len(matrix) == 2
		# 		and isinstance(matrix[0], int) 
		# 		and isinstance(matrix[1], int)):
			print(type(matrix))


class Matrix:
	def __init__(self, matrix, shape = None):
		""" 
			Matrix class that allow to make operation between them 
			self.data
			self.shape 
		"""
		if (isinstance(matrix, tuple) \
				and len(matrix) == 2 \
				and isinstance(matrix[0], int) \
				and isinstance(matrix[1], int) \
				and isinstance(shape, type(None))):
			self.data = matrix[0] * [[float(0.0) for i in range(0, matrix[1])]]
			self.shape = matrix 
		elif isinstance(matrix, list) \
				and isinstance(matrix[0], list) \
				and isinstance(shape, type(None)):
			self.data =	matrix
			self.shape = (len(matrix), len(matrix[0]))
		elif isinstance(matrix, list) \
				and isinstance(matrix[0], float) \
				and isinstance(shape, type(None)):
			self.data =	matrix
			self.shape = (1, len(matrix))
		elif isinstance(matrix, list) \
				and isinstance(shape, tuple) \
				and len(matrix) == shape[0] \
				and len(matrix[0]) == shape[1]:
			self.data = matrix
			self.shape = shape
		else:
			raise TypeError("Wrong Init Variables")
		# self.shape = (len(self.data), len(self.data[0]))		
		
	def __str__(self):
		return ("Matrix {}".format(self.data))

	def __repr__(self):
		print(self)

	def __add__(self, oth):
		""" Matrix + Matrix operation """
		if (isinstance(oth, list) and self.shape[1] == len(oth)  and self.shape[0] == 1):
			return self + Matrix(oth)
		elif (isinstance(oth, Matrix) and self.shape == oth.shape and self.shape[0] > 1):
			return Matrix([ [self.data[i][j] + oth.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
		elif (isinstance(oth, Matrix) and self.shape == oth.shape and self.shape[0] == 1):
		 	return Matrix([[self.data[0][j] + oth[0][j] for j in range(self.shape[1])]])
		else:
			raise TypeError("You can only addition 2 Matrix of the same size")
	def __radd__(self, oth):
		""" Matrix + Matrix operation """
		return self + oth

	def __sub__(self, oth):
		""" Matrix - Matrix operation """
		if (isinstance(oth, list) and self.shape[1] == len(oth)  and self.shape[0] == 1):
			return self - Matrix(oth)
		elif (isinstance(oth, Matrix) and self.shape == oth.shape and self.shape[0] > 1):
			return Matrix([ [self.data[i][j] - oth.data[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])
		elif (isinstance(oth, Matrix) and self.shape == oth.shape and self.shape[0] == 1):
		 	return Matrix([[self.data[0][j] - oth[0][j] for j in range(self.shape[1])]])
		else:
			raise TypeError("You can only sub 2 Matrix of the same size")
	
	def __rsub__(self, oth):
		""" int - Matrix operation """
		return (-1) * self + oth
	
	def __truediv__(self, oth):
		""" Matrix / int or Matrix (m*n) / Matrix (n*m) operation """
		if (isinstance(oth, Matrix) and self.shape[0] == oth.shape[1] and self.shape[1] == oth.shape[0]):
			tmp_list = []
			for k in range(self.shape[0]):
				tmp_list2 = []
				for i in range(self.shape[0]):
					tmp_val = 0
					for j in range(self.shape[1]):
						tmp_val += (self.data[j][i] / oth.data[i][j])
					tmp_list2.append(tmp_val)
				tmp_list.append(tmp_list2)
			return tmp_list
		elif ((isinstance(oth, int) or isinstance(oth, float)) and oth != 0):
			return Matrix([ [self.data[i][j] / float(oth) for j in range(self.shape[1])] for i in range(self.shape[0])])
		else:
			raise TypeError("Wrong variables for div")
	
	def __mul__(self, oth):
		""" Matrix * int or Matrix * Matrix operation """
		if (isinstance(oth, Matrix) and self.shape[0] == oth.shape[1] and self.shape[1] == oth.shape[0]):
			tmp_list = []
			for k in range(self.shape[0]):
				tmp_list2 = []
				for i in range(self.shape[0]):
					tmp_val = 0
					for j in range(self.shape[1]):
						tmp_val += (self.data[j][i] * oth.data[i][j])
					tmp_list2.append(tmp_val)
				tmp_list.append(tmp_list2)
			return tmp_list
		elif ((isinstance(oth, int) or isinstance(oth, float)) and oth != 0):
			return Matrix([ [self.data[i][j] * float(oth) for j in range(self.shape[1])] for i in range(self.shape[0])])
		else:
			raise TypeError("Wrong variables for mul")
	def __rmull__(self, oth):
		""" int * Matrix operation """
		return self + oth
	
			


	