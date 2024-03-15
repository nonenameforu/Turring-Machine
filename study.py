from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk

class ui():
    def __init__(self) :
        self.root = Tk()
        self.root.title("test_for_tkinter")
        self.root.geometry("1208x720")
        #self.root.resizable(False,False)
        self.root.iconbitmap("resorse/free-icon-turing-1875989.ico")
        
        self.entry = Entry(self.root)
        #self.entry.grid(row=1,column=1)
        
        
        
        # img = PilImage.open(r"resorse/free-icon-turing-1875989.png") открыетие 
        # img = img.resize((20,20),PilImage.ADAPTIVE) и изменение  размера фото 
        # self.image = ImageTk.PhotoImage(img) присовоение в переменную даной фотографии для того чтобы потом можно было ее использовать 
        
        ##self.label = Label(self.root, text="first_label",wraplength=20)
        ## лейбл для вывода фото  self.image = PhotoImage(file="resorse/free-icon-turing-1875989.png")
        ## здесь то же самое self.label = Label(self.root, image=self.image)
        

    def run (self):
        self.draw_widget()
        self.root.mainloop()
        
    def draw_widget(self):
        
        for i in range(100):
            text = " "+str(i)+" "
            self.label = Label(self.root, text=text,bg="red",padx=10).grid(row=0, column=i,padx=5)
            
        for i in range(5):
            self.entry.grid(row=1,column=i)
        
        
        
        #Button(self.root, text="444", command=self.button_action).grid(row=0, column=0)
        
         
        #Button(self.root, image=self.image, command=self.button_action).grid(row=0, column=0) #создание и отрисовка кнопки 
        
        # self.label = Label(self.root, text="first_label",bg="red").grid(row=0, column=0)
        # self.label2 = Label(self.root , text="second_label", bg="green").grid(row=0, column=1)
        # self.Label3 = Label(self.root, text="third_label",bg="yellow").grid(row=1,column=0)
        # self.label4 = Label(self.root, text="fouth_label",bg="pink").grid(row=1, column=1)
    
    def button_action(self):
        text = self.entry.get()
        self.label = Label(self.root, text=text,bg="red").grid(row=0, column=1)
        print()
    
if __name__ =="__main__":
    window = ui()
    window.run()
    
    