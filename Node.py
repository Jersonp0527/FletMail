class Node:
    def __init__(self, data: object = None):
        self.Data = data
        self.Next = None

    def setData(self, data: object):
        self.Data = data

    def setNext(self, Next: object):
        self.Next = Next

    def getData(self):
        return self.Data

    def getNext(self):
        return self.Next
