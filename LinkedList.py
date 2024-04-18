from dataclasses import dataclass
from typing import List, Union
import random

@dataclass(order=True)
class Elem:
    data: str

class ArrayNonSeq:
    def __init__(self, capacity=10) -> None:
        self.capaity = capacity
        self.arr: List[Union[Elem, None]] = [None] * capacity
        self.link = [-1] * capacity
        self.first = -1
    
    def getIndex(self):
        indexes = [i for i, val in enumerate(self.arr) if not val]
        if not indexes:
            raise Exception("add from full array")
        return random.choices(indexes).pop()
    
    def add(self, data):
        index = self.getIndex()
        
        bgn = self.first
        while bgn > -1 and self.link[bgn] > -1:
            bgn = self.link[bgn]
        
        self.arr[index] = Elem(data)
        if bgn < 0:
            self.first = index
            return
        self.link[bgn] = index
    
    def insert(self, data):
        prev = bgn = self.first
        elem = self.arr[bgn]
        while bgn > -1 and elem is not None and elem < Elem(data):
            prev = bgn
            bgn = self.link[prev]
            elem = self.arr[bgn]

        index = self.getIndex()
        
        self.arr[index] = Elem(data)
        if bgn == prev:
            self.link[index] = bgn
            self.first = index
        else:
            self.link[prev], self.link[index] = index, self.link[prev]
        
    def delete(self, data):
        prev = bgn = self.first
        
        elem = self.arr[bgn]
        while bgn > -1 and elem is not None and elem != Elem(data):
            prev = bgn
            bgn = self.link[prev]
            elem = self.arr[bgn]
        
        if bgn < 0: #if array is empty
            return
        
        if prev == bgn:
            self.first = self.link[bgn]
        
        self.link[prev] = self.link[bgn]
        self.link[bgn] = -1
        self.arr[bgn] = None
    
    def __str__(self):
        ret = []
        bgn = self.first
        while bgn > -1:
            ret.append(self.arr[bgn])
            bgn = self.link[bgn]
        ret = ", ".join(map(str, ret))
        return f"[{ret}]"

if __name__ == "__main__":
    SIZE = 8
    arr = ArrayNonSeq(SIZE)
    
    arr.insert("B")
    arr.add("E")
    arr.insert("F")
    arr.insert("C")
    arr.insert("A")
    arr.add("H")
    arr.insert("A")
    print(f"non-sequential array:")
    print(f"arr = {arr}")
    
    arr.delete("A")
    arr.delete("A")
    arr.delete("E")
    arr.delete("C")
    arr.delete("F")
    print(f"deleted:")
    print(f"arr = {arr}")