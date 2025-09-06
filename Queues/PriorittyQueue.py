import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def enqueue(self,data,priority):
        heapq.heappush(self.heap,(priority,data))
        self.size += 1
        print(f"Enqueued data: {data}")
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue Empty - can not dequeue")
        priority, data = heapq.heappop(self.heap)
        self.size -= 1
        return data,priority
    def peek(self):
        if self.is_empty():
            raise ValueError("Queue empty - cannot peek")
        return self.heap[0][1], self.heap[0][0]
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue (priority,data)")
        elements = sorted(self.heap)
        for priority,data in elements:
            print(f" Priority-{priority} : Data-{data}")
        print(f"Size: {self.size}")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("3. PRIORITY QUEUE:")
    pq = PriorityQueue()
    
    # Lower numbers = higher priority
    pq.enqueue("Emergency Task", 1)
    pq.enqueue("Normal Task", 5)
    pq.enqueue("High Priority", 2)
    pq.enqueue("Low Priority", 10)
    
    pq.display()
    
    print(f"\nHighest priority task: {pq.peek()}")
    while not pq.is_empty():
        task, priority = pq.dequeue()
        print(f"Processing: {task} (Priority: {priority})")
    