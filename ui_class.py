import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x800")
        self.title("Turring machine")
        
        ## Первый Фрейм ----------------------------------------------------------------------------------------------
        self.Fist_frame = CTk.CTkFrame(master=self, fg_color="black").pack(side = "top", fill= "both", expand = True)
        
        
        ## Второй Фрейм ------------------------------------------------------------------------------------------------
        self.Second_frame = CTk.CTkFrame(master=self,height=50)
        self.delete_last_state = CTk.CTkButton(master=self.Second_frame,height=10, width=50, text="Delete last state")
        self.Add_states = CTk.CTkButton(master=self.Second_frame, height=10, width=50, text="Add state")
        self.Start_machine = CTk.CTkButton(master=self.Second_frame, height=10, width=50, text="Start")
        
        self.delete_last_state.pack(side= "right",padx = 5)
        self.Add_states.pack(side= "right",padx = 5)
        self.Start_machine.pack(side= "left",padx = 5)
        self.Second_frame.pack(side = "top", fill= "x")
        
        
        ## Третий фрейм ----------------------------------------------------------------------------------------------
        self.Third_frame = CTk.CTkTabview(master=self)
        self.Third_frame.pack( side = "top", fill= "both", expand = True)
        self.Third_frame.add("Q1")
        self.Third_frame.add("Q2")
        
        
        
        # self.scrol = CTk.CTkFrame(self.Third_frame.tab("Q1"))
        # self.ctk_textbox_scrollbar = CTk.CTkScrollbar(self.scrol,command=self.scrol,activate_scrollbars=False)
        # self.scrol.configure(yscrollcommand=self.ctk_textbox_scrollbar.set)
        # self.ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ne")
        #
        # self.scrol_hor = CTk.CTkScrollableFrame(self.scrol,orientation="horizontal")
        
        # for i in range(30):
        #     #for j in range (30):
        #     enry = CTk.CTkEntry(self.scrol)
        #     enry.grid(row = 0, column = i)
        
        # self.scrol.pack(fill= "both")
        # self.scrol_hor.pack(fill= "both")

        
        # 
        # 
        
        ## Четверый фрейм -------------------------------------------------------------------------------------------
        self.Fourth_frame = CTk.CTkFrame(master=self,height=50)
        
        self.Add_comand = CTk.CTkButton(master=self.Fourth_frame,height=10, width=50, text="Add comand",command=self.Button_Add_comand)
        self.Delete_comand = CTk.CTkButton(master=self.Fourth_frame,height=10, width=50, text="Delete comand")
        
        self.Add_tape = CTk.CTkButton(master=self.Fourth_frame,height=10, width=50, text="Add tape")
        self.Delete_tape = CTk.CTkButton(master=self.Fourth_frame,height=10, width=50, text="Delete tape")
        
        self.Get_string = CTk.CTkEntry(master=self.Fourth_frame)
        self.set_start = CTk.CTkEntry(master=self.Fourth_frame)
        #self.set_start.configure(state = "0")
        self.set_tape = CTk.CTkComboBox(master=self.Fourth_frame, state="readonly",values=["tape 1"])
        self.Give = CTk.CTkButton(self.Fourth_frame,width=50, text="Give")
        
        self.Add_comand.pack(side = "left",padx = 5)
        self.Delete_comand.pack(side = "left",padx = 5)
        self.Get_string.pack(side = "left",padx = 15)
        self.set_start.pack(side = "left",padx = 5)
        self.set_tape.pack(side = "left",padx = 15)
        self.Delete_tape.pack(side = "right",padx = 5)
        self.Add_tape.pack(side = "right",padx = 5)
        
        self.Fourth_frame.pack(side = "bottom", fill= "x")

    def Button_Add_comand (self):
        self.ori = "horizontal"
        
        
        
        
        
        # self.main_frame = CTk.CTkFrame(master=self , fg_color="black")
        # self.main_frame.pack(side = "top", fill= "both", expand = True)
        
        
        # self.tab_control = CTk.CTknote
        # self.main_frame_bottom = CTk.CTkFrame(master = self)
        # self.main_frame_bottom.pack(side = "top", fill= "both", expand = True)
        
        # self.combo = CTk.CTkComboBox(self.main_frame,values=("1","2","3"),state="readonly")
        # self.combo.grid(row = 1, column = 1)
        
        
        
        # self.Button = CTk.CTkButton(self.main_frame_bottom,text="gggg")
        # self.Button.grid(row = 0 , column = 0)
        
        
        

        
    
        

        
        
        
        
        
        
        
        
        
app = App()
app.mainloop()