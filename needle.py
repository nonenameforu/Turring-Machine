import numpy as np
class needle:
    def __init__(self):
        self.L = [[["","",""],
                   ["","",""]],
                  [["","",""],
                   ["","",""]]]
        
    
    def new_condition(self):
        self.L.append([])
    
    def new_order(self, i):
        self.L[i].append([])
    
    def set_needle_derective(self, i, j, der):
        self.L[i].insert(j, der)
    
    def get_needle_derective(self, i, j):
        return self.L[i][j]




    
       

a = needle()

print(a.L)
a.new_order(0)
a.new_condition()
print(a.L)