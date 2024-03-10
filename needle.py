import string
import re
import Class_Lent
import numpy as np
class needle:
    score = int(0)
    def __init__(self):
        
        self.index_of_condition = 0
        self._L = [[["qr>","ab<","","0"],
                   ["","","","0"]],
                  
                  [["","","","1"],
                   ["","","","1"]],
                  
                  [["","","","2"],
                   ["","","","2"]]]
        self.tape = Class_Lent.lent_turring()
    
    @classmethod
    def Increment_score(cls):##Увеличение счета выполненных операций
        cls.score +=1
    @classmethod    
    def get_score(cls):## Вывод счеты выволненных операций
        return cls.score
        
    def new_condition(self):##Создание нового состояния
        self._L.append([])
    
    def del_condition(self, i):##Удаление состояния по индексу
        self._L.pop(-i)
            
    def new_order(self, i):##Создание новой команды
        self._L[i].append([])
    
    def del_order(self, i, j):##Удаление команды по индексу
        self._L[i].pop(-j)
    
    def new_tape(self):##Создание новой ленты в наборе деректив
        for sublistL in self._L:
            for sublist in sublistL:
                sublist.insert(-1,"")
        
    def del_tape(self):##Удаление ленты в наборе деректив по индексу
        for sublistL in self._L:
            for sublist in sublistL:
                sublist.pop(-2)
    
    def set_needle_derective(self, i, j, der):## Установка дерективы
        if len(der) == 3 and der.endswith(('>','<','_')) == True:
            self._L[i].insert(j, der)
            
    def get_needle_derective(self, i, j):## Взятие дерективы
        return self._L[i][j]
    
    
    def _New_tape(self, prev):##Создние новой ленты внутреннее
        new_tape = Class_Lent.lent_turring
        new_tape.set_next_tape(prev)
        prev.set_next_tape(new_tape)
        
    def create_tape(self):##создание новой ленты внешнее
        Next = self.New_tape(self.tape)
        Next.set_tape_Index(self.tape.get_tape_Index()+1)
        self.tape = Next    
    def Move_Next(self):##Перемещение на новую ленту
        Next = self.tape.get_next_tape()
        ##if (Next == None):
        ##else:
        self.tape = Next
    
    def Move_Prev(self):##Перемещение на предыдущую ленту
        Prev = self.tape.get_prev_tape()
        self.tape = Prev

    def delete_tape(self):##Удаление лнты
        while(self.tape.Next_Lent != None):
            self.Move_Next()
        if(self.tape.Next_Lent == None):

            self.Move_Prev
            self.tape.Next_Lent = None
            
a = needle()

    
print(a.L)