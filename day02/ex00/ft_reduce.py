#!/usr/bin/python

def ft_reduce(function_to_apply, list_of_inputs):
	result = 0
	for i in range(len(list_of_inputs) - 1):
		if i == 0:
			result = function_to_apply(list_of_inputs[i], list_of_inputs[i + 1])
		else:
			result = function_to_apply(result, list_of_inputs[i + 1])
		yield result

verif = lambda x, y: x + y

lst = [i for i in range(10)]

print(list(ft_reduce(verif, lst)))
# lol