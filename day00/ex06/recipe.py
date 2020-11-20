#!/usr/bin/python2.7

cookbook = dict()
c = dict()

s = {}

cookbook["sandwich"] = {"ingredients":["ham", "bread", "cheese", "tomatoes"], "meal":"lunch", "prep":10}

cookbook["cake"] = {"ingredients":["flour", "sugar", "eggs"], "meal":"dessert", "prep":60}

cookbook["salad"] = {"ingredients":["avocado", "arugula", "tomatoes", "spinach"], "meal":"lunch", "prep":15}


def init_dic(dic, key, value):
    """ Fonction that create had the key:value to dic"""
    dic[key]=value

def show_dic(dic):
    for k1, v1 in dic.items():
        print("Key={} Value={}".format(k1, v1))


init_dic(s, "ingredients", ["ham", "bread", "cheese", "tomatoes"])
init_dic(s, "meal", "lunch")
init_dic(s, "prep", 10)

init_dic(c, "sandwich", s)

show_dic(c)

