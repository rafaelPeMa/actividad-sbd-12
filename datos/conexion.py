import mysql.connector

class Conexion:

    __db = None
    __cursor = None
    __usuario = 'rperez'
    __password = 'rperez123'
    __nombredb = 'mascotas'

    def __init__(self):        
        self.__db = mysql.connector.connect(
            user = self.__usuario,
            password = self.__password,
            database = self.__nombredb
        )
        self.__cursor = self.__db.cursor()

    def commit(self):
        self.__db.commit()

    def close(self):
        self.__db.close()

    def getCursor(self):
        return self.__cursor
