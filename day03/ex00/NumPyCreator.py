import numpy as np

class NumPyCreator:
	def __init__(self):
		pass

	def from_list(self, lst, dty=None):
		return np.array(lst, dtype=dty)
	
	def from_tuple(self, tpl, dty=None):
		return np.array(tpl, dtype = dty)

	def from_iterable(self, itr, dty=None):
		return np.array(itr, dtype=dty)

	def from_shape(self, shape, val=0, dty=None):
		return np.full(shape, value=val, dtype = dty)

	def random(self, shape, dty=None):
		return np.empty(shape, dtype=dty)

	def identity(self, n, dty=None):
		return np.identity(n, dtype=dty)

	

