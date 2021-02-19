#!/usr/bin/python

class Evaluator:
	""" Class Evaluator with two static functions
		zip_evaluate
		enumerate_evaluate """
	def zip_evaluate(coefs, words):
		if (len(words) != len(coefs)):
			print(-1)
		else:
			val_ret = 0
			for elem in zip(words, coefs):
				val_ret += len(elem[0]) * elem[1]
			print(val_ret)

	def enumerate_evaluate(coefs, words):
		if (len(words) != len(coefs)):
			print(-1)
		else:
			val_ret = 0
			for one, two in enumerate(words):
				val_ret += coefs[one] * len(two)
			print(val_ret)

	enumerate_evaluate = staticmethod(enumerate_evaluate)
	zip_evaluate = staticmethod(zip_evaluate)

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)

words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
Evaluator.enumerate_evaluate(coefs, words)

