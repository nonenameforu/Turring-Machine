import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

class ui:
    def __init__(self) -> None:
        self.State = int(1)
        self.Tape = int(1)
        self.Comand = int(1)
        
        
        self.Main_Window  =tk.Tk()

        self.Fist_Frame = ttk.Frame(self.Main_Window)
        self.Second_Frame = tk.Frame(self.Main_Window, height=50)
        
        self.Third_Frame = ttk.Notebook(self.Main_Window)
        self.Fouth_Frame = tk.Frame(self.Main_Window, height=50)
        
    
    def Draw_Fist_Frame(self):
        
        canvas = tk.Canvas(self.Fist_Frame)
        scrollbar = ttk.Scrollbar(self.Fist_Frame, orient="vertical", command=canvas.yview)
        scrollbar_hor = ttk.Scrollbar(self.Fist_Frame, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="center")

        canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar_hor.set)

        
        scrollbar.pack(side="right", fill="y")
        scrollbar_hor.pack(side="bottom", fill="x")
        self.Fist_Frame.pack(fill="both",expand=True)
        canvas.pack(side="top", fill="both",expand=True)

        for i in range(25):
            for j in  range (25):
                ttk.Entry(scrollable_frame).grid(row=i, column=j,padx=10, pady=10)

        self.Fist_Frame.pack(side="top",fill="both",expand=1)
    
    def Draw_Second_Frame(self):
        Add_State = tk.Button(self.Second_Frame,text="Add State", command=self.Button_Add_State)
        Delete_Last_State = tk.Button(self.Second_Frame,text="Delete last state", command=self.Button_Delete_Last_State)
        Start = tk.Button(self.Second_Frame,text="Start", command=self.Button_Start)
        
        Delete_Last_State.pack(side="right")
        Add_State.pack(side="right",padx=10)
        Start.pack(side="left")
        self.Second_Frame.pack(side="top",fill="x")
        
    def Draw_Third_Frame(self):
        
        
        add1 = tk.Frame(self.Third_Frame,bg="#404040")
        self.Third_Frame.add(add1,text='Q1')
        
        canvas = tk.Canvas(add1)
        scrollbar = ttk.Scrollbar(add1, orient="vertical", command=canvas.yview)
        scrollbar_hor = ttk.Scrollbar(add1, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="center")

        canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=scrollbar_hor.set)

        
        scrollbar.pack(side="right", fill="y")
        scrollbar_hor.pack(side="bottom", fill="x")
        canvas.pack(side="top", fill="both",expand=True)

        for i in range(25):
            for j in  range (25):
                ttk.Entry(scrollable_frame).grid(row=i, column=j,padx=10, pady=10)
        
        
        

        self.Third_Frame.pack(side="top",fill="both",expand=1)
        

        

        
        
        

        
    def Draw_Fouth_Frame(self):
        Add_Comand = tk.Button(self.Fouth_Frame, text="Add comand", command=self.Button_Add_Command)
        Delete_comand = tk.Button(self.Fouth_Frame, text="Delete comand", command=self.Button_Delete_Last_Comand)
        
        Add_Tape = tk.Button(self.Fouth_Frame, text="Add tape", command=self.Button_Add_Tape)
        Delete_Tape = tk.Button(self.Fouth_Frame, text="Delete tape", command=self.Button_Delete_Tape)
        
        self.Give_Main_String = tk.Entry(self.Fouth_Frame)
        self.Set_Start = tk.Entry(self.Fouth_Frame)
        self.Set_Tape = ttk.Combobox(self.Fouth_Frame, state="readonly", values=["tape 1"])
        Give = tk.Button(self.Fouth_Frame, text="Give")
        
        Add_Comand.pack(side="left",padx=10)
        Delete_comand.pack(side="left")
        
        
        self.Give_Main_String.pack(side="left",padx=10)
        self.Set_Start.pack(side="left")
        self.Set_Tape.pack(side="left",padx=10)
        Give.pack(side="left")
        
        Add_Tape.pack(side="right", padx=10)
        Delete_Tape.pack(side="right")
        
        self.Fouth_Frame.pack(side="top",fill="x")
    
    
    def Draw_Main_Window(self):
        self.Main_Window.geometry("960x800")
        self.Main_Window.iconbitmap(default="resorse/free-icon-turing-1875989.ico")
        self.Main_Window.configure(bg="#3B3B3B")
        self.Main_Window.title("Машина Тьюринга")
    
    def run(self):
        
        self.Draw_Fist_Frame()
        self.Draw_Second_Frame()
        self.Draw_Third_Frame()
        self.Draw_Fouth_Frame()
        self.Draw_Main_Window()
        self.Main_Window.mainloop()
        
        
    def Button_Start(self):
        pass
        
    def Button_Add_State(self):
        self.State+=1
        new_frame = tk.Frame(self.Third_Frame)
        self.Third_Frame.add(new_frame,text="Q"+str(self.State))
        print(self.State)
    
    def Button_Delete_Last_State(self):
        if self.State>1:
            self.State-=1
            self.Third_Frame.forget(self.State)
            print(self.State)
        else:
            showinfo(title="Info", message="You can't delete more tapes")
            
            
    def Button_Add_Command(self):
        self.Comand+=1
        
    def Button_Delete_Last_Comand(self):
        self.Comand-=1
        
    def Button_Add_Tape(self):
        self.Tape+=1
        values=["tape 1","tape 2"]
        self.Set_Tape.set(values)
        
    def Button_Delete_Tape(self):
        self.Tape-=1
        
    def Button_Give(self):
        pass
        
        
        
        
if __name__ == "__main__":
    app = ui()
    app.run()