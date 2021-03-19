import numpy as np

class ColorFilter:
	def __init__(self):
		pass

	def invert(self, array):
		c_array = array
		return  1 - c_array

	def to_green(self, array):
		array_c = np.array([0, 1, 0])
		return array * array_c

	def to_red(self, array):
		return array - self.to_green(array) - self.to_blue(array)

	def to_blue(self, array):
		c_array = array
		for x_color in c_array:
			for y_color in x_color:
				y_color[0], y_color[1] = 0.0, 0.0
		return c_array

	def to_celluloid(self, array):
		""" Not Good """
		c_array = 1 - array
		for x_color in c_array:
			for y_color in x_color:
				y_color += 0.1
		return 1 - c_array