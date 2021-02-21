#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from random import randint

def log(fonction):
	def fct_sub(*args, **kwargs):
		bfr = time.time()
		ret = fonction(*args, **kwargs)
		afr = time.time()

		with open("machine.log", "a") as my_file:
			lst_name_fct = fonction.__name__.split("_")
			lst_name_fct = [elem.capitalize() for elem in lst_name_fct]
			name_fct = ""
			for elem in lst_name_fct:
				name_fct += elem + " " 
			msg = "(ymanzi)Running: {}      [ exec-time = {} ms ]\n".format(name_fct, afr - bfr)
			my_file.write(msg)
			my_file.close
		return ret
	return fct_sub


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
      if self.water_level > 20:
          return True
      else:
          print("Please add water!")
          return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)