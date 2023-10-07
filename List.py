from Node import Node


class List:
    def __init__(self):
        self._Head = Node()
        self._Tail = Node()
        self._Size = 0

    def size(self) -> int:
        return self._Size

    def isEmpty(self) -> bool:
        return self._Size == 0

    def setSize(self, s: int):
        self._Size = s

    def First(self):
        return self._Head

    def Last(self):
        return self._Tail

    def addFirst(self, e: object):
        new_node = Node(e)
        if self.isEmpty():
            self._Head = new_node
            self._Tail = new_node
        else:
            new_node.setNext(self._Head)
            self._Head = new_node
        self._Size += 1

    def addLast(self, e: object):
        new_node = Node(e)
        if self.isEmpty():
            self._Head = new_node
            self._Tail = new_node
        else:
            self._Tail.setNext(new_node)
            self._Tail = new_node
        self._Size += 1

    def removeFirst(self):
        if not self.isEmpty():
            temp = self._Head
            self._Head = temp.getNext()
            temp.setNext(None)
            self._Size -= 1
            return temp.getData()
        else:
            return None

    def removeLast(self):
        if self._Size == 1:
            return self.removeFirst()
        else:
            temp = self._Tail
            anterior = self._Head

            while anterior.getNext() != self._Tail:
                anterior = anterior.getNext()

            anterior.setNext(None)
            self._Tail = anterior
            self._Size -= 1
            return temp.getData()
