from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    data: int | None = None
    link: Node | None = None
    
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        
        return self.data == other.data
    
    def __str__(self):
        return f"{self.data}"

class ListLinkedSingly:
    def __init__(self):
        self.head = None
    
    def empty(self):
        return self.head == None
    
    def search(self, data):
        bgn = self.head
        while bgn:
            if bgn.data == data:
                return True
            
            bgn = bgn.link
        
        return False
    
    def insert_head(self, data):
        if self.empty():
            self.head = Node(data, None)
            return
        
        self.head = Node(data, self.head)
        
    def insert_tail(self, data):
        bgn = self.head
        
        while bgn and bgn.link:
            bgn = bgn.link
        
        if self.empty():
            self.head = Node(data, None)
            return 
        
        bgn.link = Node(data, None) # type: ignore
        
    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty single linked list")
        
        if not self.search(after):
            raise Exception(f"{after} is not in list")
        
        bgn = self.head
        
        while bgn and bgn.data != after:
            bgn = bgn.link

        bgn.link = Node(data, bgn.link)  # type: ignore
    
    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty single linked list")
        
        if not self.search(data):
            raise Exception(f"{data} is not in list")
        
        bgn = self.head
        prev = self.head
        
        while bgn and bgn.link and bgn.data != data:
            prev = bgn
            bgn = prev.link
        
        if prev == bgn:
            self.head = bgn.link # type: ignore
            return

        prev.link = bgn.link # type: ignore
    
    def __str__(self):
        ret = []
        bgn = self.head
        while bgn:
            ret.append(bgn)
            bgn = bgn.link
        
        ret = ", ".join(map(str, ret))
        return f"[{ret}]"

if __name__ == "__main__":
    llist = ListLinkedSingly()
    print(f"list = {llist}")
    
    data = 10
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    
    data = 20
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    
    data = 30
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    
    data = 40
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    
    data = 50
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    
    data = 60
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    
    data, after = 100, 30
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    
    data, after = 200, 60
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    
    data, after = 300, 200
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    
    data, after = 400, 50
    llist.insert(data, after)
    print(f">> llist.insert({data}, {after})")
    print(f"llist = {llist}")
    
    
    
    data = 30
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    
    data = 400
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    
    data = 70
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    
    data = 60
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    
    data = 70
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    
    data = 200
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")