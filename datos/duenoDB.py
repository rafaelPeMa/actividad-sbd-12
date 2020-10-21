from datos.conexion import Conexion
from dominio.dueno import Dueno

class DuenoDB:

    __SQL_INSERT = 'INSERT INTO dueno (nombres, apellidos, domicilio, email, telefono, \
                    foto, usuario, password) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s )'

    __SQL_SELECT = 'SELECT * FROM dueno'

    def __init__(self, conexion: Conexion):
        self.__conexion = conexion

    def insertarDueno(self, dueno: Dueno):
        cursor = self.__conexion.getCursor()
        cursor.execute(self.__SQL_INSERT,
            ( dueno.getNombres(),
              dueno.getApellidos(),
              dueno.getDomicilio(),
              dueno.getEmail(),
              dueno.getTelefono(),
              dueno.getFoto(),
              dueno.getUsuario(),
              dueno.getPassword() 
            ))
        self.__conexion.commit()
        return cursor.rowcount

    def obtenerDuenos(self):
        duenos = []

        cursor = self.__conexion.getCursor()
        cursor.execute(self.__SQL_SELECT)

        for row in cursor.fetchall():
            dueno = Dueno()
            dueno.setIdDueno(row[0])
            dueno.setNombres(row[1])
            dueno.setApellidos(row[2])
            dueno.setDomicilio(row[3])
            dueno.setEmail(row[4])
            dueno.setTelefono(row[5])
            dueno.setFoto(row[6])
            dueno.setUsuario(row[7])
            dueno.setPassword(row[8])
            duenos.append(dueno)

        return duenos
