class CircularArrayQueue:
    def __init__(self,capacity = 10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front  = 0
        self.rear  = -1
        self.size = 0
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def get_size(self):
        return self.size 
    
    def enqueue(self,data):
        if self.is_full():
            raise OverflowError("Queue too full")
        self.rear = (self.rear + 1)%self.capacity
        self.queue[self.rear] = data
        self.size += 1
        print(f"Enqueued data: {data}")
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue empty - cant delete")
        deleted_data = self.queue[self.front]
        self.queue[self.front] = None
        self.front =(self.front + 1)% self.capacity
        self.size -= 1
        return deleted_data
    
    def peek_front(self):
        if self.is_empty():
            raise ValueError("Queue empty- can not peek_front")
        return self.queue[self.front]

    def peek_rear(self):
        if self.is_empty():
            raise ValueError("Queue empty- can not peek_rear")
        return self.queue[self.rear]
    
    def display(self):
        if self.is_empty():
            print("Queue empty - cannot display")
            return
        print("Circular array queue:")
        elements = ["_"] * self.capacity
        current = self.front
        for _ in range(self.size):
            elements[current] = str(self.queue[current])
            current = (current + 1)% self.capacity
        print("Indices: "+" ".join(f"{current:2d}" for current in range(self.capacity)))
        print("Queue: [" + "][".join(f"{item:2s}" for item in elements)+"]")
        print(f"         {'F':>3}" + " " * (self.front * 3) + 
            f"{'R':>3}" if self.front != self.rear else f"F/R")
        print(f"Size: {self.size}/{self.capacity}")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("2. CIRCULAR ARRAY QUEUE:")
    ca_queue = CircularArrayQueue(capacity=5)
    
    for i in range(1, 6):
        ca_queue.enqueue(f"Item{i}")
    
    ca_queue.display()
    
    print(f"Dequeued: {ca_queue.dequeue()}")
    print(f"Dequeued: {ca_queue.dequeue()}")
    ca_queue.enqueue("NewItem1")
    ca_queue.enqueue("NewItem2")
    ca_queue.display()