import string
import re
import Class_Lent
import numpy as np
class needle:
    score = int(0)
    def __init__(self):
        self.command_index = 0
        self.index_of_condition = 0
        ##self._L = [[["","","","0"],
        ##           ["","","","0"]],
        ##          
        ##          [["","","","1"],
        ##           ["","","","1"]],
        ##          
        ##          [["","","","2"],
        ##           ["","","","2"]]]
        self.L = [[["* 8 _", "1"]
                   ]]
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
    
        self._L[i].pop(-j)
    
    def new_tape(self):##Создание новой ленты в наборе деректив
        for sublistL in self._L:
            for sublist in sublistL:
                sublist.insert(-1,"")

        
    def del_tape(self):##Удаление ленты в наборе деректив по индексу
        for sublistL in self._L:
            for sublist in sublistL:
                sublist.pop(-2)
                
    def actions_set(self, val):
        self.tape.Cell.set_Main_cell(val)
        
    def logic(self):
        switch = True
        negative_balls = int(0)
        buff = []
        while switch == True:
            
            
            ##or i in range(len(self.L[self.index_of_condition])):
            for tape in range(len(self.L[self.index_of_condition][self.command_index])):
                buff.append((self.L[self.index_of_condition][self.command_index][tape]).split(" "))
                
            
                
            while buff[tape][0] == self.tape.Cell.get_Main_cell:
                
                self.tape.Cell.set_Main_cell(buff[tape][1])
                match buff[tape][2]:
                    case '>':
                        self.tape.Move_Right    
                    case '<':
                        self.tape.Move_Left     
                    case '_':
                        pass
                if tape < len(self.L[self.index_of_condition][self.command_index])-2:    
                    tape +=1
                else:
                    tape = 0
                
                if self.tape.Next_Lent != None: 
                    self.Move_Next
                else:
                    while self.tape.Perv_Lent != None:
                        self.Move_Prev
                if buff[tape][len(self.L[self.index_of_condition][self.command_index])-1] != '0':        
                    self.index_of_condition = int(buff[tape][len(self.L[self.index_of_condition][self.command_index])-1])                 
                else:
                    switch = False 
            
            if self.command_index < len(self.L[self.index_of_condition]):
                self.command_index +=1
            else:
                self.command_index = 0
            
            

    def set_needle_derective(self, i, j, der):## Установка дерективы
        if len(der) == 5 and der.endswith(('>','<','_')) == True:
            self._L[i].insert(j, der)
            
    def get_needle_derective(self, i, j):## Взятие дерективы
        return self._L[i][j]
    
    def del_needle_derective(self, i, j):
        self._L[i][j] == "* * _"
    
    def _New_tape(self, prev):##Создние новой ленты внутреннее
        new_tape = Class_Lent.lent_turring
        new_tape.set_next_tape(prev)
        prev.set_next_tape(new_tape)
        
    def create_tape(self):##создание новой ленты внешнее
        Next = self.New_tape(self.tape)
        Next.set_tape_Index(self.tape.get_tape_Index()+1)
        self.tape = Next    
    def Move_Next(self):##Перемещение на следующую ленту
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