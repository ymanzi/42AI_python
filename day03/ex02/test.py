#!/usr/bin/python

import numpy as np
from ScrapBooker import ScrapBooker
tst = ScrapBooker()

array = np.array([list(range(6)),list(range(6, 12))])
# print(array)
print(tst.mosaic(array, (2, 2)))