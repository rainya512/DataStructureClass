class Node:
    def __init__(self, data=None, llink=None, rlink=None):
        self.data = data
        self.llink = llink
        self.rlink = rlink
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.data == other.data
    
    def __str__(self):
        return f"{self.data}"

class ListLinkedDoublyCircular:
    def __init__(self):
        self.head = None
    
    def empty(self):
        return self.head is None
    
    def search(self, data):
        if self.empty():
            return False
        
        bgn = self.head
        while bgn.rlink != self.head:
            if bgn.data == data:
                return True
            
            bgn = bgn.rlink
        
        if bgn.data == data:
            return True

        return False

    
    def insert_head(self, data):
        new = Node(data)
        
        if self.empty():
            new.llink = new
            new.rlink = new
            self.head = new
            return
        
        new.rlink = self.head
        new.llink = self.head.llink
        self.head.llink = new
        self.head = new
        self.head.llink.rlink = self.head
    
    def insert_tail(self, data):        
        if self.empty():
            self.insert_head(data)
            return
        
        new = Node(data)
        new.rlink = self.head
        new.llink = self.head.llink
        self.head.llink.rlink = new
        self.head.llink = new
    
    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty linked list")
        
        bgn = self.head
        while bgn.rlink != self.head and bgn.data != after:
            bgn = bgn.rlink
        
        if bgn == self.head.llink:
            self.insert_tail(data)
            return
        
        new = Node(data)
        new.llink = bgn
        new.rlink = bgn.rlink
        bgn.rlink.llink = new
        bgn.rlink = new
    
    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty linked list")
        
        bgn = self.head
        while bgn.rlink != self.head and bgn.data != data:
            bgn = bgn.rlink
        
        if bgn == self.head:
            bgn.rlink.llink = bgn.llink
            bgn.llink.rlink = bgn.rlink
            self.head = bgn.rlink
            return
        
        if bgn == self.head.llink:
            if self.head.llink.data != data:
                return
            
            bgn.llink.rlink = self.head
            self.head.llink = bgn.llink
            return
        
        bgn.llink.rlink = bgn.rlink
        bgn.rlink.llink = bgn.llink
    
    def __str__(self):
        res = []
        
        if self.empty():
            return f"{res}"
        
        bgn = self.head
        while bgn.rlink != self.head:
            res.append(bgn)
            bgn = bgn.rlink
        
        res.append(bgn)
        
        res = ", ".join(map(str, res))
        return f"[{res}]"

if __name__ == "__main__":
    llist = ListLinkedDoublyCircular()
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
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    
    data, after = 200, 60
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    
    data, after = 300, 200
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    
    data, after = 400, 50
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    
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