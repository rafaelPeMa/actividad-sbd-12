
class Dueno:

    def __init__(self):
        self.__idDueno = -1
        self.__nombres = ''
        self.__apellidos = ''
        self.__domicilio = ''
        self.__email = ''
        self.__telefono = ''
        self.__usuario = ''
        self.__password = ''
        self.__foto = ''

    def setIdDueno(self, idDueno): 
        self.__idDueno = idDueno

    def setNombres(self, nombres): 
        self.__nombres = nombres

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def setDomicilio(self, domicilio): 
        self.__domicilio = domicilio

    def setEmail(self, email): 
        self.__email = email

    def setTelefono(self, telefono): 
        self.__telefono = telefono

    def setUsuario(self, usuario): 
        self.__usuario = usuario

    def setPassword(self, password): 
        self.__password = password
            
    def setFoto(self, foto): 
        self.__foto = foto

    def getIdDueno(self): 
        return self.__idDueno 

    def getNombres(self): 
        return self.__nombres

    def getApellidos(self):
        return self.__apellidos

    def getDomicilio(self): 
        return self.__domicilio

    def getEmail(self): 
        return self.__email

    def getTelefono(self): 
        return self.__telefono

    def getUsuario(self): 
        return self.__usuario

    def getPassword(self): 
        return self.__password
            
    def getFoto(self): 
        return self.__foto

    def toString(self):
        tmp = str(self.__idDueno) + " | "
        tmp += self.__nombres + " | "
        tmp += self.__apellidos + " | "
        tmp += self.__domicilio + " | "
        tmp += self.__email + " | "
        tmp += self.__telefono + " | "
        tmp += self.__usuario + " | "
        tmp += self.__password + " | "
        tmp += self.__foto
        return tmp
        