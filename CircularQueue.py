class QueueCircular:
    def __init__(self, capacity=10) -> None:
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_ = self.near_ = 0
    
    def size(self):
        if self.near_ >= self.front_:
            return self.near_ - self.front_
        else:
            return self.capacity - (self.front_ - self.near_)
    
    def empty(self):
        return not self.size()
    
    def full(self):
        return self.size() + 1 >= self.capacity
    
    def enqueue(self, data):
        if self.full():
            raise Exception("enqueue from full queue")
        
        self.near_ = (self.near_ + 1) % self.capacity
        self.arr[self.near_] = data
    
    def dequeue(self):
        if self.empty():
            raise Exception("dequeue from empty queue")
        
        self.front_ = (self.front_ + 1) % self.capacity
        return self.arr[self.front_]
    
    def front(self):
        return self.arr[(self.front_+1) % self.capacity]
    
    def near(self):
        return self.arr[self.near_]
    
    def __str__(self):
        res = []
        for i in range(1, self.size()+1):
            res.append(self.arr[(self.front_+i) % self.capacity])
        
        res = ", ".join(map(str, res))
        
        return f"[{res}]"

if __name__ == "__main__":
    SIZE = 8
    queue = QueueCircular(SIZE)
    print(f"queue = {queue}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "A"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "B"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "C"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "D"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "E"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "F"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "G"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "H"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "I"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    print(f">> queue.dequeue() = {queue.dequeue()}")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()
    
    data = "J"
    queue.enqueue(data)
    print(f">> queue.enqueue({data})")
    print(f">> queue.cursor:{queue.front_, queue.near_}")
    print(f">> queue.data:{queue.front(), queue.near()}")
    print(f">> queue.status:{queue.empty(), queue.full()}")
    print(f">> queue = {queue}")
    print(f">> queue.size() = {queue.size()}")
    print()