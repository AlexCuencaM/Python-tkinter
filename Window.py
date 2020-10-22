from tkinter import *
from Table import *
class Window(Frame):
    """
    docstring
    """
    def __init__(self,master= None):
        Frame.__init__(self,master)
        self.master = master        
        # self.menu = Menu(self.master)

        # self.master.config(menu=self.menu)
        # self.fileMenu = Menu(self.menu)
        # self.fileMenu.add_command(label="Item")
        # self.fileMenu.add_command(label="Exit", command=self.__cerrar)
        # self.menu.add_cascade(label="File", menu=self.fileMenu)

        # self.editMenu = Menu(self.menu)
        # self.editMenu.add_command(label="Undo")
        # self.editMenu.add_command(label="Redo")
        # self.menu.add_cascade(label="Edit", menu=self.editMenu)   

        table = Table(self.master)     
        # widget can take all window
        
    def label(self,content="Label"):
        self.texto = Label(self,text="Hola tkinter")
        self.texto.place(x=0,y=30)
        
    def button(self,name="Button"):
        botoncito = Button(self, text=name, command=self.__cerrar)
        botoncito.place(x=0,y=0)
        
    def __cerrar(self):
        exit()
