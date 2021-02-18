#!/usr/bin/python2.7

inventaire = [
	("pommes", 22),
	("melons", 4),
	("poires", 18),
	("fraises", 76),
	("prunes", 51),
]

inverse = [(un,deux) for deux,un in inventaire]

inv_sor = [(un, deux) for deux, un in sorted(inverse, reverse=True)]

for elem in inv_sor:
	print(elem)

mondic = {}
mondic["lol"] = 5
mondic[5] = "lol"
for cle,val in mondic.items():
	print (cle, "   ", val)

