from Direccion import Direccion
from Fecha import Fecha


class Usuario:
    def __init__(self, nombre: str, ID: int, fecha_nac: Fecha,
                 ciudad_nac: str, tel: int, email: str, direccion: Direccion):
        self._id = ID
        self._nombre = nombre
        self._fecha_nac = fecha_nac
        self._ciudad_nac = ciudad_nac
        self._direccion = direccion
        self._tel = tel
        self._email = email

    # Métodos get
    def get_id(self) -> int:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_fecha_nac(self) -> Fecha:
        return self._fecha_nac

    def get_ciudad_nac(self) -> str:
        return self._ciudad_nac

    def get_direccion(self) -> Direccion:
        return self._direccion

    def get_tel(self) -> int:
        return self._tel

    def get_email(self) -> str:
        return self._email

    # Métodos set
    def set_id(self, nuevo_id: int) -> None:
        self._id = nuevo_id

    def set_nombre(self, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre

    def set_fecha_nac(self, nueva_fecha_nac: Fecha) -> None:
        self._fecha_nac = nueva_fecha_nac

    def set_ciudad_nac(self, nueva_ciudad_nac: str) -> None:
        self._ciudad_nac = nueva_ciudad_nac

    def set_direccion(self, nueva_direccion: Direccion) -> None:
        self._direccion = nueva_direccion

    def set_tel(self, nuevo_tel: int) -> None:
        self._tel = nuevo_tel

    def set_email(self, nuevo_email: str) -> None:
        self._email = nuevo_email

    def toString(self):
        return f"{self._nombre} {self._id} {self._fecha_nac.toString()} {self._ciudad_nac} {self._tel} {self._email} {self._direccion.toString()}"
