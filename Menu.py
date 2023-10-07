import flet as ft
from List import List
from DoubleList import DoubleList
from Registro import Registro


def main(page: ft.Page):
    page.title = "Whatsmessenger++"

    # Variables de funcionamiento
    Empleados = Registro()
    Empleados.importar("Empleados.txt")

    filePassword = open("Password.txt", "r")
    Password = DoubleList()
    for linea in filePassword:
        Password.addLast(linea)

    tbxID = ft.TextField(label="IDENTIFICACIÓN")
    tbxPassword = ft.TextField(label="CONTRASEÑA", password=True) # Oculta la entrada del usuario
    lblPrueba = ft.Text("Hola") # Usa el parámetro text para el valor inicial

    def checkUser(e):
        temp = Password.first()
        while temp is not None:
            contrasenas = temp.getData().split(' ')

            if tbxID.value == contrasenas[0] and tbxPassword.value == contrasenas[1]: # Usa el atributo value para obtener la entrada del usuario
                lblPrueba.value = f"registrado como {contrasenas[2]}"
                # Cambiar la ruta de la app
                page.update()
                break
            else:
                if tbxID is not contrasenas[0]:
                    tbxID.error_text = "ID no encontrado"
                if tbxPassword is not contrasenas[1]:
                    tbxPassword.error_text = "PASSWORD no encontrada"
                page.update()
            temp = temp.getNext()

    btnCheck = ft.ElevatedButton("Ingresar", on_click=checkUser) # Pasa una referencia de función, no una llamada de función
    page.add(tbxID, tbxPassword, btnCheck, lblPrueba)


ft.app(target=main , view=ft.AppView.WEB_BROWSER )
