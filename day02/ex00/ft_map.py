#!/usr/bin/python

def ft_map(function_to_apply, list_of_inputs):
	for elem in list_of_inputs:
		yield function_to_apply(elem)

verif = lambda x: x * x

lst = [i for i in range(10)]

print(list(ft_map(verif, lst)))
# lol