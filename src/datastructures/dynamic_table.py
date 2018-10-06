class DynamicTable:
    def __init__(self):
        self.table = []
        self.size = 0
        self.num = 0

    def __getitem__(self, index):
        return self.table[index - 1]

    def __setitem__(self, index, value):
        self.table[index - 1] = value
