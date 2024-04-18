class Queue:
    def __init__(self, capacity=10) -> None:
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front_, self.near_ = -1, -1
    
    def size(self):
        return self.near_ - self.front_
    
    def empty(self):
        return not self.size()
    
    def full(self):
        return self.near_ >= self.capacity - 1
    
    def __str__(self):
        return f"{self.arr}"
    
    def front(self):
        return self.arr[self.front_ + 1]
    
    def near(self):
        return self.arr[self.near_]
    
    def enqueue(self, item):
        if self.full():
            raise Exception("enqueue from full queue")
        
        self.near_ += 1
        self.arr[self.near_] = item
    
    def dequeue(self):
        if self.empty():
            raise Exception("dequeue from empty queue")

        i = self.front_ + 1
        res = self.arr[i]
        while i < self.near_:
            self.arr[i] = self.arr[i + 1]
            i += 1
        
        self.arr[self.near_] = None
        self.near_ -= 1
        
        return res

if __name__ == "__main__":
    SIZE = 5
    queue = Queue(SIZE)
    
    print(f"{queue}")
    print(f"queue.size() = {queue.size()}")
    print(f"queue.empty() = {queue.empty()}")
    print(f"queue.full() = {queue.full()}")
    print(f"queue.size() = {queue.size()}")
    
    for i in range(SIZE):
        queue.enqueue(i+1)

    print(f"queue.near() = {queue.near()}")
    print(f"queue.front() = {queue.front()}")
    print(f"queue.dequeue() = {queue.dequeue()}")
    print(queue)
    print(f"queue.dequeue() = {queue.dequeue()}")
    print(queue)
    print(f"queue.dequeue() = {queue.dequeue()}")
    print(queue)
    print(f"queue.dequeue() = {queue.dequeue()}")
    print(queue)
    print(f"queue.full() = {queue.full()}")