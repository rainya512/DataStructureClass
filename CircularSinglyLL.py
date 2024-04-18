class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.data == other.data
    
    def __str__(self):
        return f"{self.data}"

class ListLinkedSinglyCircular:
    def __init__(self):
        self.tail = None
    
    def empty(self):
        return self.tail is None
    
    def search(self, data):
        if self.empty():
            return False
        
        assert self.tail
        bgn = self.tail.link
        while bgn and bgn != Node(data):
            if bgn.link is self.tail.link:
                break
            bgn = bgn.link
        else:
            return True
        
        return False
    
    def insert_head(self, data):
        new = Node(data)
        if self.empty():
            self.tail = new.link = new
            return
        
        assert self.tail
        new.link, self.tail.link = self.tail.link, new
    
    def insert_tail(self, data):
        if self.empty():
            self.insert_head(data)
            return
        
        assert self.tail
        new = Node(data, self.tail.link)
        self.tail.link = new
        self.tail = new
    
    def insert(self, data, after):
        if self.empty():
            raise Exception("insert from empty linked list")
        
        assert self.tail and self.tail.link
        bgn = self.tail.link
        while bgn != Node(after):
            if bgn.link is self.tail.link:
                return
            bgn = bgn.link
        
        if bgn is self.tail:
            self.insert_tail(data)
            return
        
        new = Node(data, bgn.link)
        bgn.link = new
    
    def delete(self, data):
        if self.empty():
            raise Exception("delete from empty linked list")
        
        assert self.tail
        prev, bgn = self.tail, self.tail.link
        
        assert bgn, prev
        while bgn != Node(data):
            prev = bgn
            if bgn.link is self.tail.link:
                return
            bgn = bgn.link
        
        if bgn is bgn.link:
            self.tail, bgn = None, None
            return
        
        if bgn is self.tail:
            self.tail = prev
        
        prev.link = bgn.link
    
    def __str__(self):
        res = []
        
        if self.empty():
            return f"{res}"
        
        assert self.tail
        bgn = self.tail.link
        while bgn:
            res.append(bgn)
            bgn = bgn.link
            if bgn is self.tail.link:
                break
        
        res = ", ".join(map(str, res))
        return f"[{res}]"

if __name__ == "__main__":
    llist = ListLinkedSinglyCircular()
    print(f"list = {llist}")
    
    data = 10
    llist.insert_tail(data)
    print(f"list.insert_tail({data})")
    print(f"list = {llist}")
    data = 20
    llist.insert_head(data)
    print(f"list.insert_tail({data})")
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