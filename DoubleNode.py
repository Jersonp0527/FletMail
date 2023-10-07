class DoubleNode:
    def __init__(self,  data: object = None):
        self._Data = data
        self._Next = None
        self._Prev = None

    def setData(self, data: object):
        self._Data = data

    def setNext(self, Next):
        self._Next = Next

    def setPrev(self, prev):
        self._Prev = prev

    def getData(self):
        return self._Data

    def getPrev(self):
        return self._Prev

    def getNext(self):
        return self._Next
