#!/usr/bin/python

from Kmeans import KmeansClustering, CsvReader, crop
import numpy

with CsvReader("../resources/solar_system_census.csv", header=True) as file:
	file_data = file.getdata()
	file_h = file.getheader()
arr = numpy.array(file_data)
arr = crop(arr, arr.shape, (0,1))
tmp = KmeansClustering(ncentroid=4, max_iter=100)
tmp.fit(arr)
tmp.predict(arr)
# for elem in tmp.centroids:
	# print("\n\n\n\n", elem)
# print(len(tmp.centroids))