class Array:
    def __init__(self, length):
        self.array = list(range(length))
        self.length = length

    def __getitem__(self, index):
        return self.array[index - 1]

    def __setitem__(self, index, item):
        self.array[index - 1] = item
