from util import Element


class ChainedElement(Element):
    def __init__(self, key, data=None):
        super().__init__(key, data)
        self.next = self.prev = None
