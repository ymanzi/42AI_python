#!/usr/bin/python2.7

import sys
import string

def text_analyzer(*param):
    if len(param) > 1:
        print("ERROR")
    else:
        if len(param) == 0:
            s = input("What is the test to analyse?")
        else:
            s = param[0]
        up = 0
        low = 0
        pct = 0
        sp = 0
        car = 0
        for elem in s:
            car += 1
            if elem.isupper():
                up += 1
            elif elem.islower():
                low += 1
            elif elem.isspace():
                sp += 1
            elif elem in string.punctuation:
                pct += 1
        aff = """ The text contains {c} characters:\n \
- {u} upper letters \n \
- {l} lower letters \n \
- {p} punctuation marks \n \
- {s} spaces""".format(c=car, u=up, l=low, s=sp, p=pct)
        print(aff)
