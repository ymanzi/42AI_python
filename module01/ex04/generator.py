#!/goinfre/miniconda3/bin/python

import random

def generator(text, sep = " ", option = None):
	if ((type(option) != type(None) and option not in ["shuffle", "ordered", "unique"]) \
			or type(text) != str):
		my_list = ["ERROR"]
	else:
		my_list = text.split(sep)
		if (option == "ordered"):
			my_list = sorted(my_list)
		elif (option == "unique"):
			my_list = list(dict.fromkeys(my_list))
		elif (option == "shuffle"):
			for i in range(len(my_list)):
				a = random.randint(0, len(my_list) - 1)
				my_list[i], my_list[a] = my_list[a], my_list[i] 
	return my_list

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
	print(word)

for word in generator(text, sep=" ", option="shuffle"):
	print(word)

for word in generator(text, sep=" ", option="ordered"):
	print(word)

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
	print(word)

text = 1.0
for word in generator(text, sep=".", option="unique"):
	print(word)

