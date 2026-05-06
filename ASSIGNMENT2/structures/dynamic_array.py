# structures/dynamic_array.py
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.arr[self.size] = value
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            return "Underflow"
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def display(self):
        return self.arr[:self.size]