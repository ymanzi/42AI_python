#!/usr/bin/python2.7

import sys

if (len(sys.argv) != 3
        or sys.argv[1].isdigit()
        or not(sys.argv[2].isdigit())):
    print("ERROR")
else:
    lst = sys.argv[1].split()
    lst = [elem for elem in lst if len(elem) > int(sys.argv[2])]
    print(lst)

