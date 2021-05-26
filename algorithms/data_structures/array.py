class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        index = self.count
        self.count += 1
        if self.count == self.size:
            del self.count
            raise StopIteration
        return self.data[index]

    def __len__(self):
        return self.size
