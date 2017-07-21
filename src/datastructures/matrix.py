class Matrix:
    def __init__(self, data):
        self.data = list(list(row) for row in data)
        if len(data) > 0:
            self.rows = len(data)
            self.columns = len(data[0])
        else:
            self.rows = self.columns = 0

    @classmethod
    def of_dimensions(cls, rows, columns):
        return cls([[None] * columns] * rows)

    def __getitem__(self, indexes):
        if isinstance(indexes, tuple):
            i, j = indexes
            return self.data[i - 1][j - 1]
        return self.data[indexes - 1]

    def __setitem__(self, indexes, item):
        i, j = indexes
        self.data[i - 1][j - 1] = item
