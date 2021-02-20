#!/usr/bin/python

def what_are_the_vars(*args, **kwargs):
	tmp = ObjectC()
	for i in range(len(list(args))):
		setattr(tmp, "var_" + str(i), args[i])
	for (key, value) in kwargs.items():
		if len(key) > 3 and key[:4] == "var_":
			return None
		setattr(tmp, key, value)
	return tmp

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)