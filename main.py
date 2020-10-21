from dominio.dueno import Dueno
from datos.duenoDB import DuenoDB
from datos.conexion import Conexion

conexion = Conexion()
duenodb = DuenoDB(conexion)

while True:
    print('***** MASCOTAS ******')
    print('1) Agregar dueño')
    print('2) Mostrar dueños')
    print('0) Salir')
    op = input()

    if op == '1':
        d = Dueno()
        d.setNombres(input('Nombres: '))
        d.setApellidos(input('Apellidos: '))
        d.setDomicilio(input('Domicilio: '))
        d.setTelefono(input('Telefono: '))
        d.setEmail(input('Email: '))
        d.setUsuario(input('Usuario: '))
        d.setPassword(input('Password: '))
        d.setFoto(input('Foto: '))

        if duenodb.insertarDueno(d):
            print('Se agrego el dueño')
        else:
            print('Error agregando dueño')

    elif op == '2':
        duenos = duenodb.obtenerDuenos()
        for dueno in duenos:
            print(dueno.toString())
    elif op == '0':
        break

conexion.close()