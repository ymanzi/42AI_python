##!/usr/bin/python

from time import sleep
import sys

def progressbar(toolbar_width):
	sys.stdout.write("[%s]" % (" " * (toolbar_width + 3)))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width + 2))
	lst = ft_progress(toolbar_width + 1)
	for i in lst:
		sys.stdout.write("\b" * (toolbar_width + 3))
		sleep(0.1)
		sys.stdout.write("[")
		sys.stdout.write("=" * i + "%" + str(i * 100 / toolbar_width))
		sys.stdout.flush()
	sys.stdout.write("]\n")


def ft_progress(lst):
    for elem in range(lst):
        yield elem