from Table import *
from tkinter import *
from tkinter.ttk import *

class Result(Toplevel):
    def __init__(self,master,tema):
        self.theme = tema
        super().__init__(master = master) 
        self.title("Resultados :D")
        self.geometry("300x300")
        self.table = Table(self.theme,self)    
        
