class Matrix:
    def __init__(self, elements, first_row=1, first_column=1):
        self.elements = list(list(row) for row in elements)
        if len(elements) > 0:
            self.rows = len(elements)
            self.columns = len(elements[0])
        else:
            self.rows = self.columns = 0
        self.first_row = first_row
        self.first_column = first_column

    @classmethod
    def of_dimensions(cls, rows, columns, first_row=1, first_column=1):
        return cls([[None] * columns] * rows, first_row, first_column)

    def __getitem__(self, indexes):
        if isinstance(indexes, tuple):
            i, j = indexes
            return self.elements[i - self.first_row][j - self.first_column]
        return self.elements[indexes - self.first_row]

    def __setitem__(self, indexes, item):
        i, j = indexes
        self.elements[i - self.first_row][j - self.first_column] = item
