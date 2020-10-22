#!./myvenv/bin/python
from Window import *
from tkinter import *
from mysql.connector import *
from Table import *

def select():
    result = []
    conexion = connect(host="localhost",user="root",password="test", db="troubleshooting")
    cursor = conexion.cursor()
    cursor.execute("select codigo,descripcion from tema")
    for codigo,descripcion in cursor.fetchall():
        result[(codigo,descripcion)]

    conexion.close()
    return result

if __name__ == "__main__":        
    root = Tk()
    
    root.wm_title("App de Tik tok xd")
    root.geometry("500x500")
    
    app = Window(root)
    root.mainloop()