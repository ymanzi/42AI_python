#!/usr/bin/python2.7

# now = datetime.now()
# current_time = now.strftime("%d %B %Y %H:%M:%S")

class Book:
    """Book or recipes"""
    def __init__(self, name, r_list):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = r_list
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key,value in self.recipes_list:
            if name in value:
                print (self.recipes_list[key][name])

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for elem in self.recipes_list[recipe_type]:
            print(elem)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            assert(type(recipe) == type(Recipe))
        except AssertionError:
            print("The parameter is not a recipe")
        self.last_update = datetime.now()
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
