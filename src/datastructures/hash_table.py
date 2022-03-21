from datastructures.essential import Element


class ChainedElement(Element):
    def __init__(self, key, data=None):
        super().__init__(key, data)
        self.prev = None
        self.next = None


class FreePosition:
    def __init__(self, prev, next):
        self.taken = False
        self.prev = prev
        self.next = next


class TakenPosition:
    def __init__(self, element):
        self.taken = True
        self.element = element
        self.next = -1
