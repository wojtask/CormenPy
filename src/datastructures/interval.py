class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __str__(self):
        return '[%d, %d]' % (self.low, self.high)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.low == other.low and self.high == other.high
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.low, self.high))
