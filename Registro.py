from Usuario import Usuario
from Fecha import Fecha
from Direccion import Direccion
from DoubleList import DoubleList


class Registro:
    def __init__(self):
        self._registro = DoubleList()
        self._usuarios = DoubleList()

    # Imprime la cantidad de usuarios en el Registro
    def noRegistros(self) -> int:
        return self._registro.size()

    # Agrega un usuario al registro
    def agregar(self, usuario: Usuario):
        self._registro.addLast(usuario)
        self._usuarios.addLast(usuario.get_id())
        self.ordenar()

    # Muestra la lista de los IDs
    def mostrarUsuarios(self):
        temp = self._usuarios.first()
        if temp is not None:
            print("[", end="")
            while temp.getNext() is not None:
                print(f"{temp.getData()}, ", end="")
                temp = temp.getNext()
            print(f"{temp.getData()}", end="")
            print("]")
        else:
            print("[]")
        return self._usuarios

    # Eliminar por id
    def eliminar(self, ID: int):
        temp = self._registro.first()
        temp2 = self._usuarios.first()
        while temp is not None:
            usr = temp.getData()
            if usr.get_id() == ID:
                self._registro.remove(temp)
                self._usuarios.remove(temp2)
                break
            temp = temp.getNext()
            temp2 = temp2.getNext()

    @staticmethod
    def mid(start, last):
        if start is None or last is None:
            return None
        elif start == last:
            return start
        else:
            temp1 = start
            temp2 = start.getNext()
            while temp2 != last:
                temp2 = temp2.getNext()
                if temp2 != last:
                    temp1 = temp1.getNext()
                    temp2 = temp2.getNext()
            return temp1

    # busca un Usuario en el registro y lo retorna
    def buscarID(self, x):
        start = self._registro.first()
        last = self._registro.last()
        mid = self.mid(start, last)

        while mid is not None:
            if mid.getData().get_id() == x:
                return mid.getData().toString()  # Retorna el usuario encontrado
            elif mid.getData().get_id() < x:
                last = mid.getPrev()
            else:
                start = mid.getNext()
            mid = self.mid(start, last)

        return None  # Si no se encuentra el id, retorna None

    def guardar(self, filename: str):
        archivo = open(filename, "w")
        temp = self._registro.first()
        for i in range(self._registro.size()):
            archivo.write(str(temp.getData().toString()) + "\n")
            temp = temp.getNext()
        print(f"ARCHIVO GUARDADO EN {filename}\n")

    # Importa un Registro de un archivo de texto
    def importar(self, filename: str):
        archivo = open(filename, "r")
        for linea in archivo:
            partes = linea.strip().split(' ')
            nombre = partes[0]
            ID = int(partes[1])
            dd = int(partes[2])
            mm = int(partes[3])
            aa = int(partes[4])
            ciudad_nac = partes[5]
            tel = int(partes[6])
            email = partes[7]
            calle = partes[8]
            no_calle = partes[9]
            nomenclarura = partes[10]
            barrio = partes[11]
            urbanizacion = partes[12]
            apartamento = int(partes[13]) if partes[13] != "None" else None

            fecha_nac = Fecha(dd, mm, aa)
            direccion = Direccion(calle, no_calle, nomenclarura, barrio, ciudad_nac, urbanizacion, apartamento)

            usuario = Usuario(nombre, ID, fecha_nac, ciudad_nac, tel, email, direccion)
            self.agregar(usuario)
        self.ordenar()
        print("ARCHIVO IMPORTADO")

    # Imprime el registro
    def mostrar(self):
        temp = self._registro.first()
        while temp is not None:
            usuario = temp.getData()
            print(f"{usuario.toString()}")
            temp = temp.getNext()
        return self._registro

    # Ordenar
    def ordenarRegistro(self):
        n = self._registro.size()
        if n < 2:
            return

        for i in range(n):
            swapped = False

            current_node = self._registro.first()
            next_node = current_node.getNext()

            for j in range(n - i - 1):
                if current_node.getData().get_id() > next_node.getData().get_id():
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

    def ordenarUsuarios(self):
        n = self._usuarios.size()
        if n < 2:
            return

        for i in range(n):
            swapped = False

            current_node = self._usuarios.first()
            next_node = current_node.getNext()

            for j in range(n - i - 1):
                if current_node.getData() > next_node.getData():
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

    def ordenar(self):
        self.ordenarRegistro()
        self.ordenarUsuarios()
