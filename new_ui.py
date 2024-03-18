import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Label, font
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

class ui:
    def __init__(self) -> None:
        self.State = int(1) # Колличество состояни 
        self.Tape = int(1) # Колличество лент
        self.Comand = [1] # Колличество Комманд
        
        self.Lable_Tape_List = [] # Лист для всех лент
        self.Frame_list = [] # Лист для фреймов в ноутбуке
        self.All_ConditinAndState = [[["", "1"]]] # Лист для всех состояний
        
        
        
        self.Main_Window  =tk.Tk() #Создание Главнго окна
        
        self.MyFont = font.Font(size=16) # Переменная для хранения шрифта

        self.Fist_Frame = ttk.Frame(self.Main_Window) # Первый фрейм для лент

        self.Second_Frame = tk.Frame(self.Main_Window, height=50) # Второй фрейм для кнопок старт добавить состояние и удалить его 
        
        self.Third_Frame = ttk.Notebook(self.Main_Window) # Ноутбук по сути фрейм с вкладками в виде других фреймов
        self.Fouth_Frame = tk.Frame(self.Main_Window, height=50) # Нижний фрейм для остальнх элементов управления 
        
    
    def Draw_Fist_Frame(self): #метод для Отрисовки первого Фрейма
                
        self.Work_Frame = self.Create_Scrolable_Frame(self.Fist_Frame,"center")

        for i in range(101):
                ttk.Label(self.Work_Frame,text="_",font=self.MyFont).grid(row=0, column=i,padx=2, pady=3)
                ttk.Label(self.Work_Frame,text=str(i-50)).grid(row=1, column=i,padx=2, pady=3)

        self.Fist_Frame.pack(side="top",fill="both",expand=1)
    
    def Draw_Second_Frame(self): # Окно для отрисовки второго фрейма
        
        Add_State = tk.Button(self.Second_Frame,text="Add State", command=self.Button_Add_State)
        Delete_Last_State = tk.Button(self.Second_Frame,text="Delete last state", command=self.Button_Delete_Last_State)
        Start = tk.Button(self.Second_Frame,text="Start", command=self.Button_Start)
        
        Delete_Last_State.pack(side="right")
        Add_State.pack(side="right",padx=10)
        Start.pack(side="left")
        self.Second_Frame.pack(side="top",fill="x")
        
    def Draw_Third_Frame(self): # Отрисовка Третьего фрейма
        
        add1 = tk.Frame(self.Third_Frame)
        self.Third_Frame.add(add1,text='Q1')
        
        self.Frame_list.append(self.Create_Scrolable_Frame(add1,"nw"))
        self.Create_First_Command_Frame(self.Frame_list[0])
        
        self.Third_Frame.pack(side="top",fill="both",expand=1)
        


        
    def Draw_Fouth_Frame(self): # Отрисовка четвертого Фрейма
        
        Add_Comand = tk.Button(self.Fouth_Frame, text="Add comand", command=self.Button_Add_Command)
        Delete_comand = tk.Button(self.Fouth_Frame, text="Delete comand", command=self.Button_Delete_Last_Comand)
        
        Add_Tape = tk.Button(self.Fouth_Frame, text="Add tape", command=self.Button_Add_Tape)
        Delete_Tape = tk.Button(self.Fouth_Frame, text="Delete tape", command=self.Button_Delete_Tape)
        
        self.Give_Main_String = tk.Entry(self.Fouth_Frame)
        txt = StringVar(value="0")
        self.Set_Start = tk.Spinbox(self.Fouth_Frame, from_=-1000,to=1000,textvariable=txt, state="readonly")
        self.Set_Tape = tk.Spinbox(self.Fouth_Frame, from_=0,to=1000)
        Give = tk.Button(self.Fouth_Frame, text="Give")
        lable_text = tk.Label(self.Fouth_Frame, text="Text:")
        lable_Start = tk.Label(self.Fouth_Frame, text="Start:")
        label_tape = tk.Label(self.Fouth_Frame, text="Tape:")
        
        
        Add_Comand.pack(side="left",padx=10)
        Delete_comand.pack(side="left")
        
        lable_text.pack(side="left",padx=10)
        self.Give_Main_String.pack(side="left",padx=10)
        lable_Start.pack(side="left",padx=10)
        self.Set_Start.pack(side="left")
        label_tape.pack(side="left",padx=10)
        self.Set_Tape.pack(side="left",padx=10)
        Give.pack(side="left")
        
        Add_Tape.pack(side="right", padx=10)
        Delete_Tape.pack(side="right")
        
        self.Fouth_Frame.pack(side="top",fill="x")
    
    
    def Draw_Main_Window(self): # Отрисовка главного окна
        self.Main_Window.geometry("960x800")
        self.Main_Window.iconbitmap(default="resorse/free-icon-turing-1875989.ico")
        self.Main_Window.title("Машина Тьюринга")
    
    def run(self): # ранер для отрисовки всего в правильном порядке и запуске
        
        self.Draw_Fist_Frame()
        self.Draw_Second_Frame()
        self.Draw_Third_Frame()
        self.Draw_Fouth_Frame()
        self.Draw_Main_Window()
        self.Main_Window.mainloop()
        
        
    def Button_Start(self): # Кнопка для старта работы
        pass
        
    def Button_Add_State(self): # Кнопка для добавления состояний
        self.State+=1
        new_frame = tk.Frame(self.Third_Frame)
        self.Third_Frame.add(new_frame,text="Q"+str(self.State))
        self.Frame_list.append(self.Create_Scrolable_Frame(new_frame,"nw"))
        self.Create_First_Command_Frame(self.Frame_list[self.State-1])
    
    def Button_Delete_Last_State(self): # Кнопка для удаления состояний
        if self.State>1:
            self.State-=1
            self.Third_Frame.forget(self.State)
            self.Frame_list.pop()
        else:
            showinfo(title="Info", message="You can't delete more tapes")
            
            
    def Button_Add_Command(self): # Кнопка для добавления комманд
        self.new_order(self.correct_select())
        self.Comand[self.correct_select()]+=1
        ttk.Entry(self.Frame_list[self.correct_select()]).grid(row=(self.Comand[self.correct_select()]), column=1,padx=10, pady=10) # Поле для самой команды
        for i in range (self.Tape):
            ttk.Entry(self.Frame_list[self.correct_select()]).grid(row=(self.Comand[self.correct_select()]), column=i+2,padx=10, pady=10) # Поле для самой команды


        
        
        
    def Button_Delete_Last_Comand(self): # Кнопка для удаления комманд
        if self.Comand>1:
            self.Comand-=1
        else:
            showinfo(title="Info", message="You can't delete more Command")
        
        
    def Button_Add_Tape(self): # Кнопка для добавления Лент
        
        for i in range(101):
            ttk.Label(self.Work_Frame,text="_",font=self.MyFont).grid(row=(self.Tape**2)+1, column=i,padx=2, pady=3)
            ttk.Label(self.Work_Frame,text=str(i-50)).grid(row=(self.Tape**2)+2, column=i,padx=2, pady=3)
        
        self.Tape+=1
        for i in range(len(self.Frame_list)):
            ttk.Label(self.Frame_list[i], text="Command:Tape"+str(self.Tape), font=self.MyFont).grid(row=0, column=self.Tape+1,padx=10, pady=10)
            for j in range(self.Comand[i]):
                ttk.Entry(self.Frame_list[i]).grid(row=j+1, column=self.Tape+1,padx=10, pady=10) # Поле для самой команды
        
        
    def Button_Delete_Tape(self): # Кнопка для удаления Лент
        if self.Tape>1:
            self.Tape-=1
        else:
            showinfo(title="Info", message="You can't delete more Tape")
        
        
    def Button_Give(self): # Кнопка для проверки
        pass
        
        
    def correct_select(self):
            non_index = self.Third_Frame.select()
            non_index = non_index[len(non_index)-1]
            if non_index == 'e':
                return 0
            return (int(non_index)-1)
        
        
    def Create_Scrolable_Frame(self, Frame, ancore): # добавление к Фрейму два Скрол бара путем помещения в него других фреймов       
        canvas = tk.Canvas(Frame)
        scrollbar = ttk.Scrollbar(Frame, orient="vertical", command=canvas.yview)
        scrollbar_hor = ttk.Scrollbar(Frame, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor=ancore)

        canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar_hor.set)
        
        scrollbar.pack(side="right", fill="y")
        scrollbar_hor.pack(side="bottom", fill="x")
        canvas.pack(side="top", fill="both",expand=True)
        return scrollable_frame
        
        
    def Create_First_Command_Frame(self,Frame): # Заполнение окна для нового состояния
        ttk.Label(Frame,text="№" ,font=self.MyFont).grid(row=0, column=0,padx=10, pady=10)
        
        for i in range (500):
            ttk.Label(Frame,text=str(i+1),font=self.MyFont).grid(row=i+1,column=0,pady=10)
        
        ttk.Label(Frame,text="next order" ,font=self.MyFont).grid(row=0, column=1,padx=10, pady=10)
        
        for i in range(self.Tape):
            ttk.Label(Frame,text="Command:Tape"+str(i+1) ,font=self.MyFont).grid(row=0, column=i+2,padx=10, pady=10)
        
        
        self.Comand.append(1)
        ttk.Entry(Frame).grid(row=1, column=1,padx=10, pady=10 ) # Поле для следующего состояния
        for j in range(self.Tape):
            command = StringVar()
            ttk.Entry(Frame, textvariable=command).grid(row=1, column=j+2,padx=10, pady=10) # Поле для самой команды
        
        
        
        
        
        
    def new_condition(self):##Создание нового состояния
        self.All_ConditinAndState.append([])
    
    def del_condition(self, i):##Удаление состояния по индексу
        self.All_ConditinAndState.pop()
            
    def new_order(self, i):##Создание новой команды
        self.All_ConditinAndState[i].append([])
        
    def del_order(self, i):## Удаление Последей команды
        self.All_ConditinAndState[i].pop()
    
    def new_tape(self):##Создание новой ленты в наборе деректив
        for sublistL in self.All_ConditinAndState:
            for sublist in sublistL:
                sublist.insert(-1,"")

        
    def del_tape(self):##Удаление ленты в наборе деректив по индексу
        for sublistL in self.All_ConditinAndState:
            for sublist in sublistL:
                sublist.pop(-2)
        
        
if __name__ == "__main__":
    app = ui()
    app.run()