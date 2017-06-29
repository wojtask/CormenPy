from builtins import len


# a 1-based indexed array
class Array:
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    @classmethod
    def of_length(cls, length):
        return cls([None] * length)

    def __getitem__(self, index):
        return self.data[index - 1]

    def __setitem__(self, index, item):
        self.data[index - 1] = item
