class Direccion:
    def __init__(self, calle: str = None, noCalle: str = None, nomenclatura: str = None, barrio: str = None,
                 ciudad: str = None, urbanizacion: str = None, apartamento: str = None):
        self._calle = calle
        self._noCalle = noCalle
        self._nomenclatura = nomenclatura
        self._barrio = barrio
        self._ciudad = ciudad
        self._urbanizacion = urbanizacion
        self._apartamento = apartamento

    # Métodos get
    def get_calle(self) -> str:
        return self._calle

    def get_noCalle(self) -> str:
        return self._noCalle

    def get_nomenclatura(self) -> str:
        return self._nomenclatura

    def get_barrio(self) -> str:
        return self._barrio

    def get_ciudad(self) -> str:
        return self._ciudad

    def get_urbanizacion(self) -> str:
        return self._urbanizacion

    def get_apartamento(self) -> str:
        return self._apartamento

    # Métodos set
    def set_calle(self, calle: str):
        self._calle = calle

    def set_noCalle(self, noCalle: str):
        self._noCalle = noCalle

    def set_nomenclatura(self, nomenclatura: str):
        self._nomenclatura = nomenclatura

    def set_barrio(self, barrio: str):
        self._barrio = barrio

    def set_ciudad(self, ciudad: str):
        self._ciudad = ciudad

    def set_urbanizacion(self, urbanizacion: str):
        self._urbanizacion = urbanizacion

    def set_apartamento(self, apartamento: str):
        self._apartamento = apartamento

    def toString(self):
        return f"{self._calle} {self._nomenclatura} {self._barrio} {self._ciudad} {self._urbanizacion} {self._apartamento}"
