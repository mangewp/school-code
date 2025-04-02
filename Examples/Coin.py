#class format (often starts with uppercase letter)
#class Class_name:
#method format:
#def __init__ (self):
#create new instance:
#My_instance = Class_Name()
#My_instance.method to call instance

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
        
    def get_sideup(self):
        return self.sideup