from tkinter import *
from mysql.connector import *

class Table:
    def __init__(self,root):
        self.lista = self.select_themes()
        self.root = root
        
        rows = len(self.lista)
        columns= len(self.lista[0])
        
        for i in range(rows):
            for j in range(columns):
                self.e = Entry(self.root, width=14, 
                               font=('Arial',14))

                self.e.grid(row=i,column=j)                
                self.e.insert(END, self.lista[i][j])




    def select_themes(self):
        result = [('Id','Descripcion')]
        conexion = connect(host="localhost",user="root",password="test", db="troubleshooting")
        cursor = conexion.cursor()

        cursor.execute("select codigo,descripcion from tema")        
        for codigo,descripcion in cursor.fetchall():            
            result.append([codigo,descripcion])                
        conexion.close()

        return result    



if __name__ == "__main__":
    print("Hey, no estás en main xd")
    

