import string
import re
import Class_Lent
import numpy as np
class needle:
    def __init__(self):
        self.actions = ["<", "_", ">", "*"]
        self.L = [[["qr>","ab<",""],
                   ["","",""]],
                  [["","",""],
                   ["","",""]]]
        self.tape = Class_Lent.lent_turring()
        
    
    def new_condition(self):
        self.L.append([])
    
    def new_order(self, i):
        self.L[i].append([])
    
    def set_needle_derective(self, i, j, der):
        if str.len(der) == 3 and der.endswith(('>','<','_')) == True:
            self.L[i].insert(j, der)
            
        
    
    def get_needle_derective(self, i, j):
        return self.L[i][j]
    
    ##def set_letter(self, lttr):
    ##    self.alphabet.append(lttr)
    
    
    ##def get_letter(self, i):
    ##    return self.alphabet[i]
    
NDL = needle()




    
       



print(a.L)
print(a.L)