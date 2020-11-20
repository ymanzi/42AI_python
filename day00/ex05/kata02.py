#!/usr/bin/python2.7

t = (3,30,2019,9,25)

msg = "{d:02d}/{m}/{y} {h:02d}:{mi}".format(d=t[3], m=t[4], y=t[2], h=t[0], mi=t[1])
print(msg)
