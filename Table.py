from tkinter import *
class Table:
    def __init__(self,tema,root):        
        self.theme = tema
        self.lista = self.theme.select_all()
        self.root = Frame(root)
        self.root.place(x=0,y=0)
        self.rows = len(self.lista)
        self.columns= len(self.lista[0])
        
        for i in range(self.rows):
            for j in range(self.columns):
                self.e = Entry(self.root, width=14, 
                               font=('Arial',14))

                self.e.grid(row=i,column=j)                
                self.e.insert(END, self.lista[i][j])    

if __name__ == "__main__":
    print("Hey, no estás en main xd")
    

