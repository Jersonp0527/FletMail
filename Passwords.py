from Password import Password
from DoubleList import DoubleList


class Passwords:
    def __init__(self):
        self.Passwords = DoubleList()

    def agregar(self, UsrPass: Password):
        self.Passwords.addLast(UsrPass)
        self.ordenar()

    def importar(self, FileName):
        usuario = open(FileName, "r")
        for linea in usuario:
            partes = linea.strip().split(' ')
            ID = int(partes[0])
            Pass = partes[1]
            Type = partes[2]

            password = Password(ID, Pass, Type)
            self.agregar(password)

    def mostrar(self):
        temp = self.Passwords.first()
        while temp is not None:
            usuario = temp.getData()
            print(f"{usuario.toString()}")
            temp = temp.getNext()
        return self.Passwords

    def ordenar(self):
        n = self.Passwords.size()
        if n < 2:
            return

        for i in range(n):
            swapped = False

            current_node = self.Passwords.first()
            next_node = current_node.getNext()

            for j in range(n - i - 1):
                if current_node.getData().ID > next_node.getData().ID:
                    # Swap the elements if they are in the wrong order
                    current_node_data = current_node.getData()
                    next_node_data = next_node.getData()

                    current_node.setData(next_node_data)
                    next_node.setData(current_node_data)

                    swapped = True

                current_node = next_node
                next_node = next_node.getNext()

            # If no two elements were swapped in the inner loop, the list is already sorted
            if not swapped:
                break

    def guardar(self, filename: str):
        archivo = open(filename, "w")
        temp = self.Passwords.first()
        for i in range(self.Passwords.size()):
            archivo.write(str(temp.getData().toString()) + "\n")
            temp = temp.getNext()

    def buscarID(self, ID: int) -> bool:
        temp = self.Passwords.first()
        for _ in range(self.Passwords.size()):
            if temp.getData().ID == ID:
                return temp.getData()
            temp = temp.getNext()
        return False

    def eliminar(self, ID: int):
        temp = self.Passwords.first()
        while temp is not None:
            usr = temp.getData()
            if usr.ID == ID:
                self.Passwords.remove(temp)
                break
            temp = temp.getNext()
