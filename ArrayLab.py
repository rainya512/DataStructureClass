from typing import Iterable

class Array(Iterable):
    def __init__(self, capacity=10, fill=None):
        self.capacity = capacity
        self.fill = fill
        
        self.arr = [fill] * self.capacity
        self.cursor = 0
    
    def get(self, index):
        return self.arr[index]
        
    def set(self, index, value):
        self.arr[index] = value
    
    def add(self, value):
        if self.cursor >= len(self.arr):
            self.arr += [self.fill] * self.capacity
        
        self.set(self.cursor, value)
        self.cursor += 1
    
    def insert(self, index, value):
        self.add(None)
        
        i = len(self.arr) - 1
        while i >= index:
            self.arr[i] = self.arr[i - 1]
            i -= 1
        
        self.arr[index] = value
    
    def __str__(self) -> str:
        if not len(self.arr):
            return "[]"
        
        res = "["
        
        for i in self.arr:
            res += f"{i}, "
        res += "\b\b]"

        return res
    
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.arr):
            result = self.arr[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

SIZE = 5
arr = Array(SIZE)
print(arr)

for i in range(5):
    arr.add(i * 5)
print(f"arr = {arr}")

for i in arr:
    print(f"elem = {i}")
print(f"arr = {arr}")

for index, i in enumerate(arr):
    print(f"arr[{index}] = {i}")

sum_ = sum(arr)
print(f"sum = {sum_}")