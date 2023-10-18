class Password:
    def __init__(self, ID: int, Pass: str, Type: str):
        self._ID = ID
        self._Pass = Pass
        self._Type = Type

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def Pass(self):
        return self._Pass

    @Pass.setter
    def Pass(self, value):
        self._Pass = value

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, value):
        self._Type = value

    def toString(self):
        return f"{self._ID} {self._Pass} {self._Type}"
