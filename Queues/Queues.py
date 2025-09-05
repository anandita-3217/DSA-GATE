""" Linked List implentation of Queues """
class Node:
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next
    def __str__(self):
        return str(self.data)
    
class LLQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        """Add an element to the rear of the queue - O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued data: {data}")
    
    def dequeue(self):
        """Remove and return the front element - O(1)"""
        if self.is_empty():
            raise ValueError("Queue is Empty- Cannot Dequeue!")
        deleted_data = self.front.data
        self.front =self.front.next
        
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return deleted_data
    
    def peek_front(self):
        if self.is_empty():
            raise ValueError('Queue is empty- cannot peek_front')
        return self.front.data
    
    def peek_rear(self):
        if self.is_empty():
            raise ValueError('Queue is empty- cannot peek_back')
        return self.rear.data
    
    def display(self):
        """Display the queue from front to rear"""
        if self.is_empty():
            print("Queue Empty!- What u want see la!")
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Queue: [" + " <- ".join(elements) + "]")
        print("       FRONT" + " " * (len(" <- ".join(elements)) - 8) + "REAR")
        print(f"Size: {self.size}")

if __name__ == "__main__":
    print("=== QUEUE IMPLEMENTATIONS DEMONSTRATION ===\n")
    
    # 1. Linked List Queue
    print("1. LINKED LIST QUEUE:")
    ll_queue = LLQueue()
    
    for i in range(1, 6):
        ll_queue.enqueue(f"Task{i}")
    
    ll_queue.display()
    
    print(f"\nFront element: {ll_queue.peek_front()}")
    print(f"Rear element: {ll_queue.peek_rear()}")
    
    print(f"Dequeued: {ll_queue.dequeue()}")
    print(f"Dequeued: {ll_queue.dequeue()}")
    ll_queue.display()
