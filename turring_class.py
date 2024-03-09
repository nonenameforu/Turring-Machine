import Class_Cell

class lent_turring:## КЛАСС ЛЕНТЫ МАШИНЫ ТЬЮРИНГA  ----------------------------------------------------
    def __init__(self) :
       self.Cell = Class_Cell.cell()
       self.Cell.set_Index(0)
       
       
    def New_Cell_Right(self, prev):
        new_right = Class_Cell.cell()
        new_right._left_cell = prev
        return new_right
        
    def New_Cell_Left(self, prev):
        new_left = Class_Cell.cell()
        new_left._left_cell = prev
        return new_left
        
    