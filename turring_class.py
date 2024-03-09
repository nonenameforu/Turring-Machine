class cell:## КЛАСС ЯЧЕЙКИ ДЛЯ ЛЕНТЫ ТЬЮРИНГА --------------------------------------------------------
    def __init__(self) :
        self.__index = None
        
        self.__main_cell = "_"
        self.__right_cell = cell()
        self.__left_cell = cell()
        
        self.__head_cell = self.__right_cell
        self.__tail_cell = self.__left_cell
    
    ## гетеры сетеры для индекса
        
    def get_Index(self):
        return self.__index
    
    def set_Index(self, znach ):
        self.__index = int(znach)
        
    ##гетеры сетеры для главной ячейки
    
    def get_Main_cell(self):
        return self.__main_cell
    
    def set_Main_cell(self, znach):
        self.__main_cell = znach
        
    ##гетеры сетеры для правой ячейки
    
    def get_Right_cell(self):
        return self.__right_cell
        
    def set_Right_cell(self, znach):
        self.__right_cell = znach
        
    ##гетеры сетеры для левой ячейки
    
    def get_Left_cell(self):
        return self.__left_cell
    
    def set_Left_cell(self, znach):
        self.__left_cell = znach
        
    ##гетеры сетеры для самой правой ячейки
    
    def get_Head_cell(self):
        return self.__head_cell
        
    def set_Head_cell(self, znach):
        self.__head_cell = znach
    
    def __get_Head_index(self):
        return self.__head_cell.get_Index()
    
    ##гетеры сетеры для самой левой ячейки
    
    def get_Tail_cell(self):
        return self.__tail_cell
        
    def set_Tail_cell(self, znach):
        self.__tail_cell = znach
    
    def get_Tail_index(self):
        return self.__tail_cell.get_Index()
##-----------------------------------------------
class lent_turring:## КЛАСС ЛЕНТЫ МАШИНЫ ТЬЮРИНГA  ----------------------------------------------------
    def __init__(self) :
       self.Cell = cell()
       self.Cell.set_Index(0)
       
       
    def Tree2LentLEftVariant(self, befor_cell):
        Left = self.Cell.get_Left_cell()
        Left.set_Right_cell(befor_cell.get_Right_cell())
        
    def Tree2LentRightVariant(self, before_cell):
        Right = self.Cell.get_Right_cell(before_cell.get_LEft_cell())
        Right.set_Left_cell()
        
    def HowLongLenta(self):
       first = self.Cell.get_Tail_index()
       second = self.Cell.get_Head_cell()
       first *=-1
       return first+second
        
    def NewRightCell(self):
        Most_right = self.Cell.set_Head_cell()
        