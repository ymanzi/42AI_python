from math import sqrt
from math import pow

def mean(x):
	if len(x) == 0:
		return None
	mean = float(0)
	for elem in x:
		mean += elem
	return float(mean / len(x))


def median(x):
	if len(x) == 0:
		return None
	y = sorted(x)
	if (len(y) % 2):
		ret = y[int(len(x) / 2)]
	else:
		ret = (y[int(len(x) / 2) - 1] + y[int(len(x) / 2)]) / 2
	return float(ret)

def quartiles(x, percentile):
	if len(x) == 0:
		return None
	y = sorted(x)
	per = (percentile / 100) * len(y)
	if (per % 1.0):
		return float(y[int(per)])
	else:
		return float(y[int(per) - 1])

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

def std(x):
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
	return float(sqrt(ret_var / len(x)))
