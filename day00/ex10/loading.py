#!/usr/bin/python2.7
from time import sleep
import sys

def ft_progress(lst):
    for elem in lst:
        yield elem

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sys.stdout.write('\r')
    print("{}%".format(ret/20))
    sys.stdout.flush()
    sleep(0.001)
print("...")
print(ret)
