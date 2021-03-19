#!/usr/bin/python2.7

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

for cle,value in languages.items():
    msg = """{} was created by {}""".format(cle, value)
    print(msg)
