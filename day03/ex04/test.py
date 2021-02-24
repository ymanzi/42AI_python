#!/usr/bin/python

from Kmeans import KmeansClustering, CsvReader, crop
import numpy

with CsvReader("../resources/solar_system_census.csv", header=True) as file:
	file_data = file.getdata()
	file_h = file.getheader()
arr = numpy.array(file_data)
arr = crop(arr, arr.shape, (0,1))
tmp = KmeansClustering()
tmp.fit(arr)
print(tmp.centroids)
