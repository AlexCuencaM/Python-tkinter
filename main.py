#!./myvenv/bin/python
from tkinter import *
from Tema import Tema
from Table import *
from Window import Window
if __name__ == "__main__":        
    root = Tk()
    tema = Tema()    
    root.wm_title("App de Coliflor")
    root.geometry("500x500")
    app = Window(tema,root)
    root.mainloop()