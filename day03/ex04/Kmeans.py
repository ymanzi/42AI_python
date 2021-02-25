from random import randint, randrange
from math import pow, sqrt
import numpy as np

def var(x):
		if len(x) == 0:
			return None
		mean = float(0)
		for elem in x:
			mean += elem
		mean = float(mean / len(x))
		f = lambda x: pow(x - mean, 2)
		tmp_lst = list(map(f, x))
		ret_var = float(0)
		for elem in tmp_lst:
			ret_var += elem
		return float(ret_var / len(x))


def crop(array, dimensions, position=(0, 0)):
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


class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=5):
		self.ncentroid = ncentroid # number of centroids
		self.max_iter = max_iter # number of max iterations to update the centroids
		self.centroids = [] # values of the centroids
		
	def fit(self, X):
		"""
		Run the K-means clustering algorithm.
		For the location of the initial centroids, random pick ncentroids from the dataset.
		Args:
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
		None.
		Raises:
		This function should not raise any Exception.
		"""
		arr_shape = X.shape
		mean_to_centroid = None
		def get_distance(point_a, point_b):
			som = 0
			for elem in zip(point_a, point_b):
				som += pow(float(elem[0]) - float(elem[1]), 2)
			return sqrt(som)

		def get_centroid(coord, lst_centroid):
			tmp_center = lst_centroid[0]
			for elem in lst_centroid:
				if  get_distance(elem, coord) < get_distance(tmp_center, coord):
					tmp_center = elem
			return tmp_center

		def get_tuple(dic):
			tmp_list = []
			for elem in dic.values():
				som_elem = 0
				for pos in elem:
					som_elem += pos
				som_elem /= len(dic)
				tmp_list.append(som_elem)
			return tuple(tmp_list)

		for nb_iter in range(self.max_iter):
			tmp_centroids = []
			centroid_points = {}
			tmp_range = list(range(len(X)))
			for i in range(self.ncentroid):
				y = randrange(len(tmp_range))
				random_coord = tmp_range[y]
				tmp_range.pop(y)
				tmp_centroids.append(tuple(X[random_coord]))
				centroid_points[tuple(X[random_coord])] = []
			for elem in X:
				centroid_points[get_centroid(tuple(elem), tmp_centroids)].append(tuple(elem))
			tmp_mean_to_centroid = 0
			for key, value in centroid_points.items():
				mean_dict = {}
				for i in range(len(elem)):
					mean_dict[i] = []
				for i in range(len(elem)):
					mean_dict[i].append(float(elem[i]))
				key = get_tuple(mean_dict)
			tmp_centroids.clear()
			for elem in centroid_points.keys():
				tmp_centroids.append(elem)
			centroid_points.clear()
			for elem in tmp_centroids:
				centroid_points[elem] = []
			for elem in X:
				centroid_points[get_centroid(tuple(elem), tmp_centroids)].append(tuple(elem))
			for key, value in centroid_points.items():
				tmp_distance_list = []
				for elem in value:
					tmp_distance_list.append(get_distance(elem, key))
				tmp_mean_to_centroid += sqrt(var(tmp_distance_list))
			if (type(mean_to_centroid) == type(None) or tmp_mean_to_centroid < mean_to_centroid):
				mean_to_centroid = tmp_mean_to_centroid
				self.centroids.clear()
				for elem in centroid_points.values():
					self.centroids.append(elem)

	def predict(self, X):
		"""
		Predict from wich cluster each datapoint belongs to.
		Args:
		X: has to be an numpy.ndarray, a matrice of dimension m * n.
		Returns:
		the prediction has a numpy.ndarray, a vector of dimension m * 1.
		Raises:
		This function should not raise any Exception.
		"""
		# def get_avarage(lst):
		# 	tmp_dic = {}
		# 	for i in range(len(lst[0])):
		# 		tmp_dic[i] = 0.0
		# 	for elem in lst:
		# 		for i in range(len(elem)):
		# 			tmp_dic[i] += float(elem[i])
		# 	for elem in tmp_dic.values():
		# 		elem /= len(lst)
		# 	return get_tuple(tmp_dic)
		
		# def get_tuple(dic):
		# 	tmp_list = []
		# 	for elem in dic.values():
		# 		som_elem = 0
		# 		for pos in elem:
		# 			som_elem += pos
		# 		som_elem /= len(dic)
		# 		tmp_list.append(som_elem)
		# 	return tuple(tmp_list)

		# tmp_dic = {}
		# for i in range(len(self.centroids)):
		# 	tmp_dic[i] = get_avarage(self.centroids[i])
		# planet_list = ["Earth", "Venus", "Martian Republic", "Citizens of the Belt"]
		# tmp_planet = {}
		# for i in range(len(planet_list)):
		# 	tmp_planet[i] = planet_list[i]
		

		



class CsvReader():
	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.content = None
		self.file = ""
		self.header_content = ""

	def __enter__(self):
		try:
			self.file = open(self.filename, "r")
			self.content = [elem.split(self.sep) for elem in self.file.read().split('\n')]
			if (self.header):
				self.header_content = self.content.pop(0)
			if (self.skip_top and len(self.content) >= self.skip_top):
				del self.content[:self.skip_top]
				self.skip_top = 0
			while (len(self.content) and self.skip_top):
				self.content.remove(self.content[0])
				self.skip_top -= 1
			if (self.skip_bottom and len(self.content) >= self.skip_bottom):
				del self.content[-self.skip_bottom:]
				self.skip_bottom = 0
			while (len(self.content) and self.skip_bottom):
				self.content.remove(self.content[-1])
				self.skip_bottom -= 1
			size_line = len(self.content[0])
			for elem in self.content:
				if size_line != len(elem):
					return None
			return self
		except Exception:
			print("Error occured: The file can't be open", )
			return None

	def __exit__(self, exc_type, exc_value, exec_traceback):
		if type(self.content) != type(None):
			self.file.close()
	
	def getdata(self):
		return self.content

	def getheader(self):
		return self.header_content