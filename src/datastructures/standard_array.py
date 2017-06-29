from builtins import len


# a 0-based indexed (standard) array
class StandardArray:
    def __init__(self, data):
        self.data = data
        self.length = len(data)

    @classmethod
    def of_length(cls, length):
        return cls([None] * length)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, item):
        self.data[index] = item
