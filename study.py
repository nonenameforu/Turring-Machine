from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk

class ui():
    def __init__(self) :
        self.root = Tk()
        self.root.title("test_for_tkinter")
        self.root.geometry("1208x720")
        self.root.resizable(False,False)
        
        img = PilImage.open(r"resorse/free-icon-turing-1875989.png")
        img = img.resize((20,20),PilImage.ANTIALIAS)
        self.image = ImageTk.PhotoImage(img)
        
        
        ##self.label = Label(self.root, text="first_label",wraplength=20)
        ## лейбл для вывода фото  self.image = PhotoImage(file="resorse/free-icon-turing-1875989.png")
        ## здесь то же самое self.label = Label(self.root, image=self.image)
        

    def run (self):
        self.draw_widget()
        self.root.mainloop()
        
    def draw_widget(self):
        Button(self.root, width=5 ,height=1 , text="text").grid(row=0, column=0)
        
        
        # self.label = Label(self.root, text="first_label",bg="red").grid(row=0, column=0)
        # self.label2 = Label(self.root , text="second_label", bg="green").grid(row=0, column=1)
        # self.Label3 = Label(self.root, text="third_label",bg="yellow").grid(row=1,column=0)
        # self.label4 = Label(self.root, text="fouth_label",bg="pink").grid(row=1, column=1)
    
    
if __name__ =="__main__":
    window = ui()
    window.run()
    