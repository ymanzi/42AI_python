#!/usr/bin/python2.7

t = (0, 4, 132.42222, 10000, 12345.67)

msg = "day_{:02d}, ex_{:02d} : {:.2f}, {:.2e}, {:.2e}".format(t[0], t[1], t[2], t[3], t[4])
print(msg)
