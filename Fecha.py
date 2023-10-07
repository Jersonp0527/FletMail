class Fecha:
    def __init__(self, dd: int, mm: int, aa: int):
        self._dd = dd
        self._mm = mm
        self._aa = aa

    # Métodos get
    def get_dd(self) -> int:
        return self._dd

    def get_mm(self) -> int:
        return self._mm

    def get_aa(self) -> int:
        return self._aa

    # Métodos set
    def set_dd(self, nuevo_dd: int) -> None:
        self._dd = nuevo_dd

    def set_mm(self, nuevo_mm: int) -> None:
        self._mm = nuevo_mm

    def set_aa(self, nuevo_aa: int) -> None:
        self._aa = nuevo_aa

    def toString(self):
        return f"{self._dd} {self._mm} {self._aa}"
