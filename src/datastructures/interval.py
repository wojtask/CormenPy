class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __str__(self):
        return '[' + str(self.low) + ', ' + str(self.high) + ']'
