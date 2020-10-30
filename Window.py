from tkinter import *
from Result import Result
class Window(Frame):
    """
    docstring
    """
    #Widgets

    def __init__(self,tema, root= None):
        Frame.__init__(self,root)        
        self.root = root
        self.tema = tema        
        # widget can take all window
        self.label("Tema:",x=.0,y=.1) 
        self.label_tema = self.entry(x=.2,y=.2)
        self.b_insertar = self.button(lambda:self.tema.insert_tema(self.label_tema.get()),"Ingresar",x=.5,y=.2)
        
        self.label("Ingresar por Id:",x=.0,y=.3) 
        self.buscar_id_tema = self.entry(x=.2,y=.4)
        
        self.label("Modificar descripcion:",x=.0,y=.4) 
        self.modify_descripcion = self.entry(x=.2,y=.5)
        self.b_update = self.button(lambda:self.tema.update_tema(self.buscar_id_tema.get(),self.modify_descripcion.get() ), "Modificar",x=.5,y=.5)

        self.label("Borrar por Id:",x=.0,y=.6) 
        self.id_tema = self.entry(x=.2,y=.7)
        self.b_delete = self.button(lambda:self.tema.delete_tema(self.id_tema.get()), "Eliminar",x=.5,y=.7)

        self.b_result = Button(self.root,text="Ver Tabla")
        self.b_result.bind("<Button>", lambda e: Result(self.root,self.tema))                
        self.b_result.place(relx=.1,rely=.8)



    def label(self,content="Label", y=.1,x=.1):
        texto = Label(self.root,text=content)
        texto.place(relx=x,rely=y)
        return texto
    
    def entry(self,y=.1,x=.1):        
        e = Entry(self.root,textvariable=StringVar())
        e.place(relx=x,rely=y,anchor=S)        
        return e
      
    def button(self,function,name="Button",y=.1,x=.1):
        botoncito = Button(self.root, text=name, command=function)
        botoncito.place(relx=x,rely=y,anchor=S)   

    
    def __cerrar(self):
        exit()


if __name__ == "__main__":
    print("Hey, no estás en main xd")
