#!/usr/bin/python

import numpy as np
from ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")

from ColorFilter import ColorFilter
cf = ColorFilter()

# imp.display(cf.to_green(arr))
# imp.display(cf.to_blue(arr))
imp.display(cf.to_celluloid(arr))
# print(cf.to_blue(arr))