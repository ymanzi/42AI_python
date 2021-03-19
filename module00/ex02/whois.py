#!/usr/bin/python2.7

import sys

if len(sys.argv) > 2 or (len(sys.argv) == 2 and not(sys.argv[1].isdigit())):
    print "ERROR"
elif (len(sys.argv) == 2):
    a = int(sys.argv[1])
    if (a == 0):
        print "I'm Zero."
    elif (a % 2 == 0):
        print "I'm Even."
    else:
        print "I'm Odd."
