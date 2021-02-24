import matplotlib.pyplot as plt

class ImageProcessor:
	def __init__(self):
		pass

	def load(self, image_path):
		ret = plt.imread(image_path)
		print("Loading image of dimensions {} x {}".format(ret.shape[0], ret.shape[1]))
		return ret

	def display(self, arr):
		plt.imshow(arr)
		plt.show()


