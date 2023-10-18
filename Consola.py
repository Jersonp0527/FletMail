from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario
from Registro import Registro
from Password import Password
from Passwords import Passwords
import datetime
import os

# Importamos  los datos
Empleados = Registro()
Empleados.importar("Empleados.txt")

Passwords = Passwords()
Passwords.importar("Password.txt")


def checkUser(identificacion: int, password: str):
    if Passwords.buscarID(identificacion):
        temp = Passwords.Passwords.first()
        while temp is not None:
            if temp.getData().ID == identificacion and temp.getData().Pass == password:
                return temp.getData().Type
            temp = temp.getNext()
        print("Contraseña Incorrecta")
    else:
        print("ID incorrecto")


print("MENSAJERIA LOCAL")
ID = int(input("Ingrese su ID: "))
Pass = input("Ingrese su Contraseña: ")
UserType = checkUser(ID, Pass)


def Enviar(id: int, titulo: str, mensaje: str):
    now = datetime.datetime.now()
    fecha_actual = now.date()
    if os.path.exists(f"Mensajes/usr{id}") is False:
        os.mkdir(f"Mensajes/usr{id}")
        os.mkdir(f"Mensajes/usr{id}/BA")
        os.mkdir(f"Mensajes/usr{id}/ML")
        os.mkdir(f"Mensajes/usr{id}/B")
    archivo = open(f"Mensajes/usr{id}/BA/{ID}BA.txt", "w")
    archivo.write(f"{fecha_actual} {titulo} {Empleados.buscarID(ID).get_nombre()}\n{mensaje}")


def Borrador(id: int, titulo: str, mensaje: str):
    now = datetime.datetime.now()
    fecha_actual = now.date()
    archivo = open(f"Mensajes/usr{ID}/B/{id}B.txt", "w")
    archivo.write(f"{fecha_actual} {titulo} {Empleados.buscarID(ID).get_nombre()}\n{mensaje}")


while True:
    # Leer los Archivos
    if os.path.exists(f"Mensajes") is False:
        os.mkdir(f"Mensajes")

    if os.path.exists(f"Mensajes/usr{ID}") is False:
        os.mkdir(f"Mensajes/usr{ID}")
        os.mkdir(f"Mensajes/usr{ID}/BA")
        os.mkdir(f"Mensajes/usr{ID}/ML")
        os.mkdir(f"Mensajes/usr{ID}/B")

    Borradores = os.listdir(f"Mensajes/usr{ID}/B")
    Leidos = os.listdir(f"Mensajes/usr{ID}/ML")
    Bandeja = os.listdir(f"Mensajes/usr{ID}/BA")

    print("1. Mostrar Bandeja de Entrada")
    print("2. Mostrar Leidos")
    print("3. Mostrar Borradores")
    print("4. Redactar Mensaje")
    if UserType == "administrador":
        print("5. Configuraciones")
    print("x. Salir")

    opcion = input()
    if opcion == "x":
        exit()
    elif opcion == "1":
        print(Bandeja)
    elif opcion == "2":
        print(Leidos)
    elif opcion == "3":
        print(Borradores)
    elif opcion == "4":
        print("\nENVIANDO MENSAJE")
        IDenvio = int(input("ID: "))
        Titulo = input("Titulo: ")
        Mensaje = input("Mensaje: ")
        destino = input("1. Enviar mensaje \n2. Borradores \n3. Descartar\n")
        if destino == "1":
            Enviar(IDenvio, Titulo, Mensaje)
        elif destino == "2":
            Borrador(IDenvio, Titulo, Mensaje)
        else:
            continue
    elif opcion == "5":
        while True:
            opcion = input("1. Nuevos usuario \n2. Cambiar contraseñas \n3. Eliminar usuarios\n4. Regresar\n")
            if opcion == "1":
                id = int(input("ID: "))
                nombre = input("Nombre: ")

                print("Fecha de nacimiento")
                dd = int(input("Día: "))
                mm = int(input("Mes: "))
                aa = int(input("Año: "))
                fecha_nac = Fecha(dd, mm, aa)

                ciudad_nac = input("Ciudad de Nacimiento: ")

                print("Direccion")
                calle = input("Calle: ")
                noCalle = input("noCalle: ")
                nomenclatura = input("Nomenclatura: ")
                barrio = input("Barrio: ")
                ciudad = input("Ciudad: ")
                urbanizacion = input("Urbanizacion: ")
                apartamento = input("Apartamento: ")
                direccion = Direccion(calle, noCalle, nomenclatura, barrio, ciudad, urbanizacion, apartamento)

                tel = int(input("Telefono: "))
                email = input("Email: ")

                usuario = Usuario(nombre, id, fecha_nac, ciudad_nac, tel, email, direccion)

                print()
                password = input("Contraseña: ")
                tipo = "administrador" if input("Tipo de usuario \n1. Empleado \n2. Administrador \n") == "2" else "Empleado"
                contrasena = Password(id, password, tipo)

                Empleados.agregar(usuario)
                Empleados.guardar("Empleados.txt")
                Passwords.agregar(contrasena)
                Passwords.guardar("Password.txt")
            elif opcion == "2":
                id = int(input("ID: "))
                password = input("Contraseña: ")
                tipo = Passwords.buscarID(id).Type
                Passwords.eliminar(id)
                Passwords.agregar(Password(id, password, tipo))

                # Falta
            elif opcion == "3":
                id = int(input("ID: "))
                Empleados.eliminar(id)
                Empleados.guardar("Empleados.txt")
                Passwords.eliminar(id)
                Passwords.guardar("Password.txt")
            elif opcion == "4":
                break
            else:
                print("ERROR: Opción incorrecta")
    else:
        print("ERROR: Opción incorrecta")

exit()
