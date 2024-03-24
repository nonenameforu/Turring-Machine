import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Label, font
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import needle
class ui:
    def __init__(self) -> None:
        self.State = int(1) # Колличество состояни 
        self.Tape = int(1) # Колличество лент
        self.Comand = [1] # Колличество Комманд
        self.length = 201
        
        self.Tape_List = [] # Лист для всех лент
        self.Frame_list = [] # Лист для фреймов в ноутбуке
        self.All_ConditinAndState = [] # Лист для всех состояний
        self.Start_Tapes = [0]
        
        self.Main_Window  =tk.Tk() #Создание Главнго окна
        
        self.MyFont = font.Font(size=16) # Переменная для хранения шрифта

        self.Fist_Frame = ttk.Frame(self.Main_Window) # Первый фрейм для лент

        self.Second_Frame = tk.Frame(self.Main_Window, height=50) # Второй фрейм для кнопок старт добавить состояние и удалить его 
        
        self.Third_Frame = ttk.Notebook(self.Main_Window) # Ноутбук по сути фрейм с вкладками в виде других фреймов
        self.Fouth_Frame = tk.Frame(self.Main_Window, height=50) # Нижний фрейм для остальнх элементов управления 
        
    def Draw_Fist_Frame(self): #метод для Отрисовки первого Фрейма
        self.new_tape()
        self.add_viev_tape_x3(0)        
        self.Work_Frame = self.Create_Scrolable_Frame(self.Fist_Frame,"n")
        for i in range(self.length):
            Text_cell = StringVar(value="_")
            Label_for_cell = ttk.Label(self.Work_Frame,font=self.MyFont, textvariable=Text_cell)
            Label_num = ttk.Label(self.Work_Frame,text=str(i-(int((self.length-1)/2))))
            self.add_cell(Label_for_cell, 0, 0)
            self.add_cell(Label_num, 0, 1)
            self.add_cell(Text_cell, 0, 2)
            Label_num.grid(row=1, column=i,padx=2, pady=3)
            Label_for_cell.grid(row=0, column=i,padx=2, pady=3)

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
        self.Text_Set_start = StringVar(value="0")
        self.Set_Start = tk.Spinbox(self.Fouth_Frame, from_=-1000,to=1000,textvariable=self.Text_Set_start, state="readonly")
        self.Set_Tape = tk.Spinbox(self.Fouth_Frame, from_=1,to=1000)
        Give = tk.Button(self.Fouth_Frame, text="Give", command=self.Button_Give)
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
        
        State_Send = []
        Tape_Send = []
        for i in range(len(self.All_ConditinAndState)):
            State_Send.append([])
            for j in range(1,len(self.All_ConditinAndState[i])):
                State_Send[i].append([])
                for k in range(1,len(self.All_ConditinAndState[i][j])):
                    State_Send[i][j-1].append(self.All_ConditinAndState[i][j][k].get())
                    if len(State_Send[i][j-1][k-1]) != 5 or State_Send[i][j-1][k-1].endswith(('>','<','_')) == False:
                        showerror(title="Error", message="You have problem in: Q"+str(i+1)+" Comand number "+str(j)+" Tape number "+str(k))
                        return -1
            State_Send[i][j-1].append(self.All_ConditinAndState[i][j][0].get())
            if int(State_Send[i][j-1][-1])<0 or int(State_Send[i][j-1][-1])>self.State:
                showerror(title="Error", message="You have problem in: next command nomber "+str(j)+" State "+str(i+1))
                return -1
        for i in range (self.Tape):
            Tape_Send.append(self.Tape_List[i][2])
        self.logic(State_Send)


    def Button_Add_State(self): # Кнопка для добавления состояний
        self.State+=1
        new_frame = tk.Frame(self.Third_Frame)
        self.Third_Frame.add(new_frame,text="Q"+str(self.State))
        self.Frame_list.append(self.Create_Scrolable_Frame(new_frame,"nw"))
        self.Create_First_Command_Frame(self.Frame_list[self.State-1])
    
    def Button_Delete_Last_State(self): # Кнопка для удаления состояний
        if self.State>1:
            self.State-=1
            for i in range(self.Comand[-1]):
                for j in range(self.Tape):
                    self.All_ConditinAndState[-1][i][j].destroy()
            self.del_layer()
            self.Frame_list[-1].destroy()
            self.Third_Frame.forget(self.State)
            self.Frame_list.pop()
        else:
            showinfo(title="Info", message="You can't delete more tapes")
               
    def Button_Add_Command(self): # Кнопка для добавления комманд
        this_Frame_index = self.correct_select()
        self.Comand[this_Frame_index]+=1
        self.add_row(this_Frame_index)
        Entry_for_next_state = ttk.Entry(self.Frame_list[this_Frame_index])
        self.add_column(Entry_for_next_state, this_Frame_index, self.Comand[this_Frame_index])
        Entry_for_next_state.grid(row=(self.Comand[this_Frame_index]), column=1,padx=10, pady=10) # Поле Для перехода в следующее состояние
        for i in range (self.Tape):
            Entry_for_command = ttk.Entry(self.Frame_list[this_Frame_index])
            self.add_column(Entry_for_command, this_Frame_index, self.Comand[this_Frame_index])
            Entry_for_command.grid(row=(self.Comand[this_Frame_index]), column=i+2,padx=10, pady=10) # Поле для самой команды
        
    def Button_Delete_Last_Comand(self): # Кнопка для удаления комманд
        this_Frame_index = self.correct_select()
        if self.Comand[this_Frame_index]>1:
            for i in range(self.Tape+1):
                self.All_ConditinAndState[this_Frame_index][-1][i].destroy()
            self.del_row(this_Frame_index)
            self.Comand[this_Frame_index]-=1
            
        else:
            showinfo(title="Info", message="You can't delete more Command")
        
    def Button_Add_Tape(self): # Кнопка для добавления Лент
        self.Start_Tapes.append(0)
        self.new_tape()
        self.add_viev_tape_x3(self.Tape)
        for i in range(self.length):
            Text_cell = StringVar(value="_")
            Label_for_cell = ttk.Label(self.Work_Frame, textvariable=Text_cell,font=self.MyFont)
            Label_num = ttk.Label(self.Work_Frame, text=str(i-(int((self.length-1)/2))))
            
            Label_for_cell.grid(row=(self.Tape**2)+1, column=i,padx=2, pady=3)
            Label_num.grid(row=(self.Tape**2)+2, column=i,padx=2, pady=3)
            
            self.add_cell(Label_for_cell, self.Tape, 0)
            self.add_cell(Label_num, self.Tape, 1)
            self.add_cell(Text_cell, self.Tape, 2)
            
        self.Tape+=1
        
        for i in range(len(self.Frame_list)):
            Label_Command = ttk.Label(self.Frame_list[i], text="Command:Tape"+str(self.Tape), font=self.MyFont)
            self.add_column(Label_Command, i, 0)
            Label_Command.grid(row=0, column=self.Tape+1,padx=10, pady=10)
            for j in range(self.Comand[i]):
                Entry_Command = ttk.Entry(self.Frame_list[i])
                self.add_column(Entry_Command, i, j+1)
                Entry_Command.grid(row=j+1, column=self.Tape+1,padx=10, pady=10) # Поле для самой команды
                
        
    def Button_Delete_Tape(self): # Кнопка для удаления Лент
        if self.Tape>1:
            self.Start_Tapes.pop()
            for i in range(self.length):
                self.Tape_List[-1][0][i].destroy()
                self.Tape_List[-1][1][i].destroy()
        
            self.Tape_List[-1][0].pop()
            self.Tape_List[-1][1].pop()
            self.Tape_List[-1][2].pop()
            self.Tape_List.pop()
                
            for i in range(len(self.Frame_list)):
                for j in range(self.Comand[i]+1):
                    self.All_ConditinAndState[i][j][-1].destroy()
                    self.All_ConditinAndState[i][j].pop()
            self.Tape-=1
        else:
            showinfo(title="Info", message="You can't delete more Tape")
        
    def Button_Give(self): # Кнопка для проверки
        Tape_number = int(self.Set_Tape.get())
        Set_start = int(self.Set_Start.get())
        self.Start_Tapes[Tape_number-1]=Set_start
        if Tape_number<=self.Tape:
            Main_cell = self.Give_Main_String.get()
            if len(Main_cell)>int(self.length/2)-Tape_number:
                self.Extension_Tape(int(self.length/2)-Tape_number+10)
            Main_cell_index = 0
            for i in range(self.length):
                if int(Set_start)+int(self.length/2)<=i and Main_cell_index<=len(Main_cell)-1:
                    self.Tape_List[Tape_number-1][2][i].set(Main_cell[Main_cell_index])
                    Main_cell_index+=1
                else:
                    self.Tape_List[Tape_number-1][2][i].set("_")
        else:
            showinfo(title="Info", message="There is no such tape")
            
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
        self.new_layer()
        Frame_len2index = (len(self.Frame_list)-1)
        self.add_row(Frame_len2index)
        for i in range (251):
            ttk.Label(Frame,text=str(i+1),font=self.MyFont).grid(row=i+1,column=0,pady=10)
        
        Label_next_order = ttk.Label(Frame,text="next order" ,font=self.MyFont)
        self.add_column(Label_next_order, Frame_len2index, 0)

        Label_next_order.grid(row=0, column=1,padx=10, pady=10)
        
        for i in range(self.Tape):
            Labele_Comand_tape = ttk.Label(Frame,text="Command:Tape"+str(i+1) ,font=self.MyFont)
            self.add_column(Labele_Comand_tape, Frame_len2index, 0)
            Labele_Comand_tape.grid(row=0, column=i+2,padx=10, pady=10)

        self.Comand.append(1)
        self.add_row(Frame_len2index)
        Entry_next_order = ttk.Entry(Frame) # Поле для следующего состояния
        self.add_column(Entry_next_order, Frame_len2index, 1)
        Entry_next_order.grid(row=1, column=1,padx=10, pady=10 )
        for j in range(self.Tape):
            Entry_Command = ttk.Entry(Frame)
            self.add_column(Entry_Command, Frame_len2index, 1)
            Entry_Command.grid(row=1, column=j+2,padx=10, pady=10) # Поле для самой команды
            
    def new_layer(self):##Создание нового состояния
        self.All_ConditinAndState.append([])
    
    def del_layer(self):##Удаление состояния по индексу
        self.All_ConditinAndState.pop()
            
    def add_row(self, layer):##Создание новой команды
        self.All_ConditinAndState[layer].append([])
  
    def del_row(self, layer):## Удаление Последей команды
        self.All_ConditinAndState[layer].pop()
    
    def add_column(self, meaning, list, row):##Создание новой ленты в наборе деректив
        self.All_ConditinAndState[list][row].append(meaning)
        
    def del_column(self, list, row):##Удаление ленты в наборе деректив по индексу
        self.All_ConditinAndState[list][row].pop()
        
    def new_tape(self):##Создание нового состояния
        self.Tape_List.append([])
    
    def del_tape(self):##Удаление состояния по индексу
        self.Tape_List.pop()
            
    def add_viev_tape(self, layer):##Создание новой команды
        self.Tape_List[layer].append([])
        
    def add_viev_tape_x3(self, layer):
        for i in range(3):
            self.Tape_List[layer].append([])
  
    def del_viev_tape(self, layer):## Удаление Последей команды
        self.Tape_List[layer].pop()
    
    def add_cell(self, meaning, list, row):##Создание новой ленты в наборе деректив
        self.Tape_List[list][row].append(meaning)
        
    def del_cell(self, list, row):##Удаление ленты в наборе деректив по индексу
        self.Tape_List[list][row].pop()
    
    def Extension_Tape(self, how_many):
        Extension_left = []
        Extension_right = []
        for i in range(self.Tape):
            Extension_left.append([])
            Extension_right.append([])
            for j in range(int(how_many/2)):
                for k in range(3):
                    Extension_left[i].append([])
                    Extension_right[i].append([])
                
                Text_cell_left = StringVar(value="_")
                Label_for_cell_left = ttk.Label(self.Work_Frame, textvariable=Text_cell_left,font=self.MyFont)
                Label_num_left = ttk.Label(self.Work_Frame, text=str(j-int(((self.length-1)/2+(how_many/2)))))
                
                Text_cell_right = StringVar(value="_")
                Label_for_cell_right = ttk.Label(self.Work_Frame, textvariable=Text_cell_right,font=self.MyFont)
                Label_num_right = ttk.Label(self.Work_Frame, text=str(j+1+int(((self.length-1)/2))))
                
                Extension_left[i][0].append(Label_for_cell_left)
                Extension_left[i][1].append(Label_num_left)
                Extension_left[i][2].append(Text_cell_left)
                
                Extension_right[i][0].append(Label_for_cell_right)
                Extension_right[i][1].append(Label_num_right)
                Extension_right[i][2].append(Text_cell_right)
                
            for j in range(self.length):
                self.Tape_List[i][0][j].forget()
                self.Tape_List[i][1][j].forget()
        
        for i in range(self.Tape):
            self.Tape_List[i][0] = Extension_left[i][0]+self.Tape_List[i][0]+Extension_right[i][0]
            self.Tape_List[i][1] = Extension_left[i][1]+self.Tape_List[i][1]+Extension_right[i][1]
            self.Tape_List[i][2] = Extension_left[i][2]+self.Tape_List[i][2]+Extension_right[i][2]
            for j in range(how_many+self.length):
                self.Tape_List[i][0][j].grid(row=i*2, column=j,padx=2, pady=3)
                self.Tape_List[i][1][j].grid(row=(i*2)+1, column=j,padx=2, pady=3)
        self.length+=how_many
            
    def logic(self, states):
        start_position_list = self.Start_Tapes
        tape = 0
    
        condition_index = 0
        command_index = 0
        
        switch = True
        buff = []
        while switch == True:
            
            for i in range(len(states[condition_index][command_index])):
                buff.append((states[condition_index][command_index][i]).split(" "))
      
            while buff[tape][0] == self.Tape_List[tape][2][start_position_list[tape]+100].get():
                
                self.Tape_List[tape][2][start_position_list[tape]+100].set(buff[tape][1])
                match buff[tape][2]:
                    case '>':
                        start_position_list[tape]+=1    
                    case '<':
                        start_position_list[tape]-=1     
                    case '_':
                        pass
                print(len(states[condition_index][command_index])-1)    
                if tape < len(states[condition_index][command_index])-1 and tape < self.Tape:    
                    tape +=1
                else:
                    tape = 0
                
                if len(buff[tape]) == 1:
                    

                    if buff[tape][0] != '0':        
                        condition_index = int(buff[tape][0])                 
                    else:
                        switch = False
                    
                if start_position_list[tape-1] == 101:
                    switch = False
                    showerror(title="Error", message="End tape")
                    break
 
            
            if command_index < len(states[condition_index]):
                command_index +=1
            else:
                command_index = 0
                
            

if __name__ == "__main__":
    app = ui()
    app.run()