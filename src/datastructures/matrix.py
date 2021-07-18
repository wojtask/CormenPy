class Matrix:
    def __init__(self, elements):
        self.elements = list(list(row) for row in elements)
        if len(elements) > 0:
            self.rows = len(elements)
            self.columns = len(elements[0])
        else:
            self.rows = self.columns = 0

    @classmethod
    def of_dimensions(cls, rows, columns):
        return cls([[None] * columns] * rows)

    def __getitem__(self, indexes):
        if isinstance(indexes, tuple):
            i, j = indexes
            return self.elements[i - 1][j - 1]
        return self.elements[indexes - 1]

    def __setitem__(self, indexes, item):
        i, j = indexes
        self.elements[i - 1][j - 1] = item

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.rows != other.rows or self.columns != other.columns:
                return False
            for i in range(self.rows):
                if self.elements[i][:self.columns] != other.elements[i][:self.columns]:
                    return False
            return True
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.rows, self.columns, [row[:self.columns] for row in self.elements[:self.rows]]))

    def __iter__(self):
        return (row[:self.columns] for row in self.elements[:self.rows])
