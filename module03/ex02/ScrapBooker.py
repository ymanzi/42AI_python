import numpy as np

class ScrapBooker:
	def __init__(self):
		pass

	def crop(self, array, dimensions, position=(0, 0)):
		""" 
			crop(array, dimensions, position)

			crops the image as a rectangle with the given dimensions 
			(meaning, the new height and width for the image), 
			whose top left corner is given by the position argument. 
			The position should be (0,0) by default. 
			Dimensions can't be larger than the current image size.
		"""

		p0 = position[0]
		p1 = position[1]
		if (array.shape[0] < p0 or array.shape[1] < p1 ):
			raise IndexError("Position is out of the array")
		c_array = array[p0: p0 + dimensions[0], p1 : p1 + dimensions[1]]
		return c_array

	def thin(self, array, n, axis):
		"""
			thin(array, n, axis)
			
			deletes every n-th pixel row along the specified axis 
			(0 vertical, 1 horizontal), example below.
		"""

		if (axis):
			return array[:,::n]
		return array[::n,]

	def juxtapose(self, array, n, axis):
		"""
			juxtapose(array, n, axis)
			juxtaposes n copies of the image
			along the specified axis (0 vertical, 1 horizontal).
		"""
		if (axis):
			return np.array([ n * elem for elem in array.tolist()])
		return np.array(n * array.tolist())
	
	def mosaic(self, array, dimensions):
		"""
			makes a grid with multiple copies of the array.
			The dimensions argument specifies the dimensions
			(meaning the height and width) of the grid (e.g. 2x3).
		"""
		tmp = np.array(dimensions[0] * array.tolist())
		return np.array([ dimensions[1] * elem for elem in tmp.tolist()])
