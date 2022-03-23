class Element:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key and self.data == other.data
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, float):
            return self.key < other
        return self.key < other.key

    def __gt__(self, other):
        if isinstance(other, float):
            return self.key > other
        return self.key > other.key

    def __hash__(self):
        return hash((self.key, self.data))

    def __repr__(self):
        return str(self.key) + (' (%s)' % self.data if self.data is not None else '')


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%f, %f)' % (self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y))


class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __repr__(self):
        return '[%d, %d]' % (self.low, self.high)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.low == other.low and self.high == other.high
        return NotImplemented

    def __hash__(self):
        return hash((self.low, self.high))


class Activity:
    def __init__(self, id, processing_time, release_time):
        self.id = id
        self.p = processing_time
        self.r = release_time

    def __lt__(self, other):
        if isinstance(other, float):
            return self.p < other
        return self.p < other.p

    def __gt__(self, other):
        if isinstance(other, float):
            return self.p > other
        return self.p > other.p
