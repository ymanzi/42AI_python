#!/usr/bin/python

def ft_filter(function_to_apply, list_of_inputs):
	for elem in list_of_inputs:
		if function_to_apply(elem):
			yield elem

verif = lambda x: x > 5

lst = [i for i in range(10)]

print(list(ft_filter(verif, lst)))
# lol