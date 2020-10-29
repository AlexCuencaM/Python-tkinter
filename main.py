#!./myvenv/bin/python
from Window import *
from tkinter import *

from Table import *

if __name__ == "__main__":        
    root = Tk()
    
    root.wm_title("App de Tik tok xd")
    root.geometry("500x500")

    app = Window(root)
    root.mainloop()