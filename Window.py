from tkinter import *
from Table import *
class Window(Frame):
    """
    docstring
    """
    #Widgets

    def __init__(self,root= None):
        Frame.__init__(self,root)        
        self.root = root

        table = Table(self.root)     # PEP 582; used by e.g. github.com/David-OConnor/pyflow
        self.label("Tabla de contenido",x=.6,y=0)        
        # widget can take all window
        self.label("Tema:",x=.0,y=.5) 
        self.tema = self.entry(x=.2,y=.6)
        self.submit = self.button(self.insertar,"Ingresar",x=.5,y=.6)
        
    def label(self,content="Label", y=.1,x=.1):
        texto = Label(self.root,text=content)
        texto.place(relx=x,rely=y)
        return texto
        
    def button(self,function,name="Button",y=.1,x=.1):
        botoncito = Button(self.root, text=name, command=function)
        botoncito.place(relx=x,rely=y,anchor=S)    
    def insertar(self):
        self.insert_theme(self.tema.get())

    def entry(self,y=.1,x=.1):        
        e = Entry(self.root,textvariable=StringVar())
        e.place(relx=x,rely=y,anchor=S)        
        return e

    def insert_theme(self,descripcion):
        conexion = connect(host="localhost",user="root",password="test", db="troubleshooting")
        cursor = conexion.cursor()

        cursor.execute("insert into tema(descripcion,eliminado) values(%s, %s)",(descripcion,0))        
        conexion.commit()
        print(cursor.rowcount,'rows inserted')

    def __cerrar(self):
        exit()


if __name__ == "__main__":
    print("Hey, no estás en main xd")
