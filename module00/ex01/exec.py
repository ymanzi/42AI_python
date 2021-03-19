#!/usr/bin/python2.7

import sys

phr = list(sys.argv)
del phr[0]


phr = " ".join(phr)

phr = phr[::-1]

phr = phr.swapcase()

if len(phr) > 0:
    print phr
