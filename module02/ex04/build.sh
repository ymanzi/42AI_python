#!/bin/bash

#https://packaging.python.org/tutorials/packaging-projects/

mkdir dist
mkdir ai42
mkdir ai42/logging
touch ai42/__init__.py
touch ai42/logging/__init__.py
echo '# -*- coding: utf-8 -*-

import time
from random import randint

def log(fonction):
	def fct_sub(*args, **kwargs):
		bfr = time.time()
		ret = fonction(*args, **kwargs)
		afr = time.time()

		with open("machine.log", "a") as my_file:
			lst_name_fct = fonction.__name__.split("_")
			lst_name_fct = [elem.capitalize() for elem in lst_name_fct]
			name_fct = ""
			for elem in lst_name_fct:
				name_fct += elem + " " 
			msg = "(ymanzi)Running: {}      [ exec-time = {} ms ]\n".format(name_fct, afr - bfr)
			my_file.write(msg)
			my_file.close
		return ret
	return fct_sub' > ai42/logging/log.py

echo 'from time import sleep
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
        yield elem' > ai42/progressbar.py

echo 'import setuptools

setuptools.setup(
	name="ai42", # Replace with your own username
	version="1.0.0",
	author="Yves Manzi",
	author_email="yv.manzi@student.s19.be",
	description="A small example package",
	long_description="42Ai Python Bootcamp day02/ex04",
	long_description_content_type="text/markdown",
	url="https://github.com/ymanzi/bootcamp_python/blob/master/day02/ex04",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	packages=setuptools.find_packages(),
	python_requires=">=3.6",
)' > setup.py

python3 -m pip install --upgrade build
python3 -m build
rm -rf \=3.6,$'\n'\) ai42.egg-info/ build
