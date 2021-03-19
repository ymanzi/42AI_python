#!/usr/bin/python2.7

class Recipe:
    """ une classe qui va contenir les recettes
    - name (str)
    - cooking_lvl (int) : range 1 to 5
    - cooking_time (int) : in minutes (no negative numbers)
    - ingredients (list) : list of all ingredients each represented by a string
    - description (str) : description of the recipe
    - recipe_type (str) : can be "starter", "lunch" or "dessert". """
	
    def __init__(self, name, lvl, tim, ingred, desc, typ):
        try:
            self.name = str(name)
        except TypeError:
            print("The name is not a string")
        
        try:
            self.cooking_lvl = int(lvl)
            assert (1 <= int(lvl) <= 5)
        except TypeError:
            print("The cooking level is not an int")
        except AssertionError:
            print("The cooking level is not between 1 to 5")
        try:
            self.cooking_time = int(tim)
            assert (int(tim) >= 0)
        except TypeError:
            print("The cooking time is not an int")
        except AssertionError:
            print("The cooking time is not a positive number")
        self.ingredients = ingred
        try:
            assert (type(ingred) == type(list))
            if (len(ingred)) == 0:
                raise ValueError()
        except ValueError:
            print("La liste d'ingredients est vide")
        except AssertionError:
            print("The ingredients should be a list")
        self.description = desc
        self.recipe_type = typ

    def __str__(self):
        """Return the string to print with the recipe info"""
        text = "name({})\nlvl({})\ntime({})\ningredients({})\ndescription({})\nrecipe({})".format(self.name, self.cooking_level, self.cooking_time, self.ingredients, self.description, self.recype_type)
        return text

