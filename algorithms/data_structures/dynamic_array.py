from array import Array

class DynamicArray(Array):
    def __init__(self, size):
        super().__init__(size)
        self.num_items = 0
        self.resize_factor = 0.75

    def __setitem__(self, index, value):
        if value is None:
            if self.data[index] is None:
                pass
            else:
                self.data[index] = value
                self.num_items -= 1
        else:
            if self.data[index] is None:
                self.data[index] = value
                self.num_items += 1
            else:
                self.data[index] = value

        persentage_filled = self.num_items/self.size
        if self.num_items and persentage_filled > self.resize_factor:
            self._resize()

    def _resize(self):
        new_array = Array(self.size * 2)
        for i in range(self.size):
            new_array[i] = self.data[i]
        self.data = new_array
        self.size *= 2