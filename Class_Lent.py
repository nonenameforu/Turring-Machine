import Class_Cell

class lent_turring:## КЛАСС ЛЕНТЫ МАШИНЫ ТЬЮРИНГA  ----------------------------------------------------
    def __init__(self) :
        self.tape_index = None  ##Индекс этой лент
        self.Prev_Lent = None   ##Предыдущаю ленты 
        self.Next_Lent = None   ##Следующая лента
        self.Cell = Class_Cell.cell()   ##создание первой ячейки в ленте
        self.Cell.set_Index(0)  ##Обозначение Индекса для первой ячейки  
       
    
    def set_next_tape(self, znach):
        self.Next_Lent = znach
    
    def get_next_tape(self):
        return self.Next_Lent
    
    def set_perv_tape(self, znach):
        self.Perv_Lent = znach
    
    def get_perv_tape(self):
        return self.Perv_Lent
       
    def get_tape_Index(self):
        return self.tape_index
    
    def set_tape_Index(self, znach ):
        self.tape_index = int(znach)
        
    
    
    
    def _New_Cell_Right(self, prev):##Создыние новой правой ячейки
        new_right = Class_Cell.cell()
        new_right.set_Left_cell(prev) 
        prev.set_Right_cell(new_right)
        
    def _New_Cell_Left(self, prev):##Создание новой левой ячейки
        new_left = Class_Cell.cell()
        new_left.set_Right_cell(prev)
        prev.set_Left_cell(new_left)
        ##return new_left
        
    def Move_Right(self):##Перемещение ленты влево
        Right = self.Cell.get_Right_cell()
        if (Right == None):
            Right = self._New_Cell_Right(self.Cell)
            Right.set_Index(self.Cell.get_Index()+1)
            self.Cell = Right
            
        else:
            self.Cell = Right
    
    def Move_Left(self):##Перемещение Леныт впарво
        Left = self.Cell.get_Left_cell()
        if (Left == None):
            Left = self._New_Cell_Left(self.Cell)
            Left.set_Index(self.Cell.get_Index-1)
            self.Cell = Left
        else:
            self.Cell = Left
    
            
        