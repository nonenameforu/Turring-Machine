from typing import Tuple
import customtkinter as CTk

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("Turring machine")
        
    
        
        self.main_frame = CTk.CTkFrame(master=self , fg_color="black")
        self.main_frame.pack(side = "top", fill= "both", expand = True)
        
        self.main_frame_bottom = CTk.CTkFrame(master = self)
        self.main_frame_bottom.pack(side = "top", fill= "both", expand = True)
        
        
        
        
        
        
        
        
        
app = App()
app.mainloop()