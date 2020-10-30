import mysql.connector

class Tema:
    def __init__(self):
        self.__conexion = mysql.connector.connect(host="localhost",user="root",password="test", db="troubleshooting")        
    
    def select_all(self):
        result = [('Id','Descripcion')]        
        cursor = self.__conexion.cursor()
        cursor.execute("select codigo,descripcion from tema")        
        for codigo,descripcion in cursor.fetchall():            
            result.append([codigo,descripcion])                
        self.__conexion.close()

        return result
    
    def update_tema(self,id,descripcion):                
        cursor = self.__conexion.cursor()
        sql = "UPDATE tema SET descripcion=%s WHERE codigo=%s"        
        cursor.execute(sql,(descripcion,id) )
        self.__conexion.commit()
        self.__conexion.close()        
        return "%d record(s) affected" % cursor.rowcount
    
    def insert_tema(self,descripcion):
        cursor = self.__conexion.cursor()
        cursor.execute("insert into tema(descripcion,eliminado) values(%s, %s)",(descripcion,0))        
        self.__conexion.commit()
        self.__conexion.close()
        return '%d rows inserted' % cursor.rowcount
    
    def delete_tema(self, id):            
        cursor = self.__conexion.cursor()
        sql = "DELETE FROM tema WHERE id=%s"        
        cursor.execute(sql,id)
        self.__conexion.commit()
        self.__conexion.close()

        return "%d record(s) deleted" % cursor.rowcount
    

    if __name__ == "__main__":
        print("Hey, no estás en main xd")
