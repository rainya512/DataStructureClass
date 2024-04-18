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
    
class LinkListDoubly:
    def __init__(self) -> None:
        self.head = None
        
    def empty(self):
        return self.head is None
    
    def search(self, data):
        if self.empty():
            return False
        
        bgn = self.head
        while bgn:
            if bgn.data == data:
                return True
            
            bgn = bgn.rlink
        
        return False
            
    
    def insert_head(self, data):
        new = Node(data)
        
        if self.empty():
            self.head = new
            return 
        
        assert self.head
        new.rlink = self.head
        self.head.llink = new
        self.head = new
    
    def insert_tail(self, data):
        new = Node(data)
        
        if self.empty():
            self.insert_head(data)
            return
        
        bgn = self.head
        
        assert bgn  
        while bgn.rlink != None:
            bgn = bgn.rlink
        
        bgn.rlink = new
        new.llink = bgn
    
    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty linked list")
        
        bgn = self.head
        while bgn and bgn.data != after:
            bgn = bgn.rlink
        
        assert bgn
        if bgn.rlink is None:
            self.insert_tail(data)
            return
        
        assert bgn and bgn.rlink
        new = Node(data, bgn, bgn.rlink)
        bgn.rlink.llink = new
        bgn.rlink = new
        
    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty linked list")

        assert self.head
        bgn, prev = self.head, self.head
        
        while bgn and bgn.rlink and bgn.data != data:
            prev = bgn
            bgn = bgn.rlink
        
        if bgn == self.head:
            self.head = bgn.rlink
            
            if self.head is not None:
                self.head.llink = None
            
            return
        
        if bgn.rlink is None: #if data at tail
            prev.rlink = None
            return 
        
        prev.rlink = bgn.rlink
        bgn.rlink.llink = prev
        
    def __str__(self):
        res = []
        if self.empty():
            return f"{res}"
        
        bgn = self.head
        while bgn:
            res.append(bgn)
            bgn = bgn.rlink
        
        res = ", ".join(map(str, res))
        return f"[{res}]"
        
if __name__ == "__main__":
    llist = LinkListDoubly()
    print(f"list = {llist}")
    
    data = 10
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    data = 20
    llist.insert_head(data)
    print(f"list.insert_head({data})")
    print(f"list = {llist}")
    data = 30
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    
    data = 20
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    
    data, after = 20, 30
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    data, after = 40, 10
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    data, after = 50, 20
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    data, after = 60, 50
    llist.insert(data, after)
    print(f"list.insert({data}, {after})")
    print(f"list = {llist}")
    
    data = 10
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    
    data = 60
    print(f"list.search({data}) = {llist.search(data)}")
    llist.delete(data)
    print(f"list.delete({data})")
    print(f"list = {llist}")
    print(f"list.search({data}) = {llist.search(data)}")