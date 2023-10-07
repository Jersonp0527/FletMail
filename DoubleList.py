from DoubleNode import DoubleNode


class DoubleList:
    def __init__(self):
        self._Head = DoubleNode()
        self._Tail = DoubleNode()
        self._Size = 0

    def size(self):
        return self._Size

    def isEmpty(self):
        return self._Size == 0

    def first(self):
        return self._Head

    def last(self):
        return self._Tail

    def addFirst(self, data: object):
        n = DoubleNode(data)
        if self.isEmpty():
            self._Head = n
            self._Tail = n
        else:
            n.setNext(self._Head)
            self._Head.setPrev(n)
            self._Head = n
        self._Size += 1

    def addLast(self, data: object):
        n = DoubleNode(data)
        if self.isEmpty():
            self._Head = n
            self._Tail = n
        else:
            self._Tail.setNext(n)
            n.setPrev(self._Tail)
            self._Tail = n
        self._Size += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            temp = self._Head
            self._Head = temp.getNext()
            temp.setNext(None)
            self._Head.setPrev(None)
            self._Size -= 1
            return temp.getData()

    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            temp = self._Tail
            self._Tail = temp.getPrev()
            self._Tail.setNext(None)
            temp.setPrev(None)
            self._Size -= 1
            return temp

    def remove(self, n: DoubleNode):
        if n == self._Head:
            return self.removeFirst()
        elif n == self._Tail:
            return self.removeLast()
        else:
            e = n.getData()
            temp_prev = n.getPrev()
            temp_next = n.getNext()
            temp_prev.setNext(temp_next)
            temp_next.setPrev(temp_prev)
            n.setNext(None)
            n.setPrev(None)
            self._Size -= 1
            return e

    def addBefore(self, n: DoubleNode, e: object):
        if n == self._Head:
            self.addFirst(e)
        else:
            m = DoubleNode(e)
            temp_prev = n.getPrev()
            temp_prev.setNext(m)
            m.setPrev(temp_prev)
            m.setNext(n)
            n.setPrev(m)
            self._Size += 1

    def addAfter(self, n: DoubleNode, e: object):
        if n == self._Tail:
            self.addLast(e)
        else:
            m = DoubleNode(e)
            temp_next = n.getNext()
            n.setNext(m)
            m.setPrev(n)
            m.setNext(temp_next)
            temp_next.setPrev(m)
            self._Size += 1
