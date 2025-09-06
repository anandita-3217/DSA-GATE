A queue is a First-In-First-Out (FIFO) data structure where elements are added at one end (rear/back) and removed from the other end (front). Think of it like a line of people waiting - the first person in line is the first to be served.

## Types of Queue Implementations

There are several ways to implement queues, each with different trade-offs:

1. **Array-based Queue**: Simple but may have size limitations
2. **Circular Array Queue**: Efficient use of space
3. **Linked List Queue**: Dynamic size, most flexible
4. **Double-ended Queue (Deque)**: Operations at both ends## Key Queue Concepts

**Basic Operations**:
- **Enqueue**: Add element to the rear of the queue
- **Dequeue**: Remove and return element from the front
- **Front/Peek**: View the front element without removing it
- **isEmpty**: Check if queue has no elements

**FIFO Principle**: The first element added is the first element removed, like a line at a store.


```python
from collections import deque
import threading

# ============================================================================
# 1. LINKED LIST QUEUE IMPLEMENTATION
# ============================================================================

class Node:
    """Node class for linked list queue"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    """Queue implementation using a singly linked list"""
    
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue
        self.size = 0
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return self.front is None
    
    def get_size(self):
        """Return the number of elements in the queue - O(1)"""
        return self.size
    
    def enqueue(self, data):
        """Add an element to the rear of the queue - O(1)"""
        new_node = Node(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        """Remove and return the front element - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot dequeue")
        
        data = self.front.data
        self.front = self.front.next
        
        # If queue becomes empty, update rear
        if self.front is None:
            self.rear = None
        
        self.size -= 1
        return data
    
    def peek_front(self):
        """Return the front element without removing it - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot peek")
        return self.front.data
    
    def peek_rear(self):
        """Return the rear element without removing it - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot peek")
        return self.rear.data
    
    def display(self):
        """Display the queue from front to rear"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Queue: [" + " <- ".join(elements) + "]")
        print("       FRONT" + " " * (len(" <- ".join(elements)) - 8) + "REAR")
        print(f"Size: {self.size}")
    
    def clear(self):
        """Clear all elements from the queue"""
        self.front = self.rear = None
        self.size = 0

# ============================================================================
# 2. CIRCULAR ARRAY QUEUE IMPLEMENTATION
# ============================================================================

class CircularArrayQueue:
    """Queue implementation using a circular array"""
    
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_empty(self):
        """Check if queue is empty - O(1)"""
        return self.size == 0
    
    def is_full(self):
        """Check if queue is full - O(1)"""
        return self.size == self.capacity
    
    def get_size(self):
        """Return the number of elements in the queue - O(1)"""
        return self.size
    
    def enqueue(self, data):
        """Add an element to the rear of the queue - O(1)"""
        if self.is_full():
            raise OverflowError("Queue is full - cannot enqueue")
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        print(f"Enqueued: {data}")
    
    def dequeue(self):
        """Remove and return the front element - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot dequeue")
        
        data = self.queue[self.front]
        self.queue[self.front] = None  # Optional: clear the slot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data
    
    def peek_front(self):
        """Return the front element without removing it - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot peek")
        return self.queue[self.front]
    
    def peek_rear(self):
        """Return the rear element without removing it - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty - cannot peek")
        return self.queue[self.rear]
    
    def display(self):
        """Display the queue showing circular structure"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Circular Array Queue:")
        display_queue = ["_"] * self.capacity
        
        i = self.front
        for _ in range(self.size):
            display_queue[i] = str(self.queue[i])
            i = (i + 1) % self.capacity
        
        print("Indices: " + " ".join(f"{i:2d}" for i in range(self.capacity)))
        print("Queue:   [" + "][".join(f"{item:2s}" for item in display_queue) + "]")
        print(f"         {'F':>3}" + " " * (self.front * 3) + 
              f"{'R':>3}" if self.front != self.rear else f"F/R")
        print(f"Size: {self.size}/{self.capacity}")

# ============================================================================
# 3. PRIORITY QUEUE IMPLEMENTATION
# ============================================================================

import heapq

class PriorityQueue:
    """Priority Queue implementation using a min-heap"""
    
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def is_empty(self):
        """Check if priority queue is empty - O(1)"""
        return self.size == 0
    
    def get_size(self):
        """Return the number of elements - O(1)"""
        return self.size
    
    def enqueue(self, data, priority):
        """Add an element with priority - O(log n)"""
        heapq.heappush(self.heap, (priority, data))
        self.size += 1
        print(f"Enqueued: {data} with priority {priority}")
    
    def dequeue(self):
        """Remove and return the highest priority element - O(log n)"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        priority, data = heapq.heappop(self.heap)
        self.size -= 1
        return data, priority
    
    def peek(self):
        """Return the highest priority element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        return self.heap[0][1], self.heap[0][0]  # data, priority
    
    def display(self):
        """Display the priority queue"""
        if self.is_empty():
            print("Priority queue is empty")
            return
        
        print("Priority Queue (priority, data):")
        sorted_items = sorted(self.heap)
        for priority, data in sorted_items:
            print(f"  Priority {priority}: {data}")
        print(f"Size: {self.size}")

# ============================================================================
# 4. DEQUE (DOUBLE-ENDED QUEUE) IMPLEMENTATION
# ============================================================================

class DequeNode:
    """Node for doubly linked list used in deque"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    """Double-ended queue implementation using doubly linked list"""
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        """Check if deque is empty - O(1)"""
        return self.front is None
    
    def get_size(self):
        """Return the number of elements - O(1)"""
        return self.size
    
    def add_front(self, data):
        """Add element to the front - O(1)"""
        new_node = DequeNode(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        
        self.size += 1
        print(f"Added to front: {data}")
    
    def add_rear(self, data):
        """Add element to the rear - O(1)"""
        new_node = DequeNode(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        print(f"Added to rear: {data}")
    
    def remove_front(self):
        """Remove and return element from front - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        data = self.front.data
        self.front = self.front.next
        
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        
        self.size -= 1
        return data
    
    def remove_rear(self):
        """Remove and return element from rear - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        data = self.rear.data
        self.rear = self.rear.prev
        
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        
        self.size -= 1
        return data
    
    def peek_front(self):
        """Return front element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.data
    
    def peek_rear(self):
        """Return rear element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.data
    
    def display(self):
        """Display the deque"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Deque: [" + " <-> ".join(elements) + "]")
        print("       FRONT" + " " * (len(" <-> ".join(elements)) - 8) + "REAR")
        print(f"Size: {self.size}")

# ============================================================================
# QUEUE APPLICATIONS
# ============================================================================

class TaskScheduler:
    """Task scheduler using queue"""
    
    def __init__(self):
        self.task_queue = LinkedListQueue()
        self.completed_tasks = []
    
    def add_task(self, task_name, priority=1):
        """Add a task to the queue"""
        self.task_queue.enqueue((task_name, priority))
    
    def process_next_task(self):
        """Process the next task in queue"""
        if self.task_queue.is_empty():
            print("No tasks to process")
            return None
        
        task_name, priority = self.task_queue.dequeue()
        print(f"Processing task: {task_name} (Priority: {priority})")
        self.completed_tasks.append(task_name)
        return task_name
    
    def show_status(self):
        """Show current status of task scheduler"""
        print(f"Tasks in queue: {self.task_queue.get_size()}")
        print(f"Completed tasks: {len(self.completed_tasks)}")
        if self.completed_tasks:
            print(f"Last completed: {self.completed_tasks[-1]}")

class BFSGraphTraversal:
    """Breadth-First Search using queue"""
    
    def __init__(self, graph):
        self.graph = graph  # Adjacency list representation
    
    def bfs(self, start_node):
        """Perform BFS traversal starting from start_node"""
        if start_node not in self.graph:
            return []
        
        visited = set()
        queue = LinkedListQueue()
        result = []
        
        queue.enqueue(start_node)
        visited.add(start_node)
        
        while not queue.is_empty():
            current = queue.dequeue()
            result.append(current)
            
            # Add neighbors to queue
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)
        
        return result

# ============================================================================
# DEMONSTRATION AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== QUEUE IMPLEMENTATIONS DEMONSTRATION ===\n")
    
    # 1. Linked List Queue
    print("1. LINKED LIST QUEUE:")
    ll_queue = LinkedListQueue()
    
    for i in range(1, 6):
        ll_queue.enqueue(f"Task{i}")
    
    ll_queue.display()
    
    print(f"\nFront element: {ll_queue.peek_front()}")
    print(f"Rear element: {ll_queue.peek_rear()}")
    
    print(f"Dequeued: {ll_queue.dequeue()}")
    print(f"Dequeued: {ll_queue.dequeue()}")
    ll_queue.display()
    
    # 2. Circular Array Queue
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
    
    # 3. Priority Queue
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
    
    # 4. Deque
    print("\n" + "="*50)
    print("4. DEQUE (DOUBLE-ENDED QUEUE):")
    dq = Deque()
    
    dq.add_rear("Middle")
    dq.add_front("First")
    dq.add_rear("Last")
    dq.add_front("VeryFirst")
    
    dq.display()
    
    print(f"Removed from front: {dq.remove_front()}")
    print(f"Removed from rear: {dq.remove_rear()}")
    dq.display()
    
    # 5. Task Scheduler Application
    print("\n" + "="*50)
    print("5. TASK SCHEDULER APPLICATION:")
    scheduler = TaskScheduler()
    
    scheduler.add_task("Send emails", 3)
    scheduler.add_task("Generate report", 1)
    scheduler.add_task("Backup database", 2)
    
    scheduler.show_status()
    
    while scheduler.task_queue.get_size() > 0:
        scheduler.process_next_task()
    
    scheduler.show_status()
    
    # 6. BFS Graph Traversal
    print("\n" + "="*50)
    print("6. BFS GRAPH TRAVERSAL:")
    
    # Create a sample graph
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    bfs = BFSGraphTraversal(graph)
    result = bfs.bfs('A')
    print(f"BFS traversal starting from 'A': {result}")
    
    print("\n=== QUEUE DEMONSTRATIONS COMPLETE ===")

```


## Implementation Comparison

| Implementation | Enqueue | Dequeue | Space | Pros | Cons |
|----------------|---------|---------|-------|------|------|
| **Linked List** | O(1) | O(1) | Dynamic | No size limit, efficient | Extra pointer storage |
| **Circular Array** | O(1) | O(1) | Fixed | Memory efficient | Fixed capacity |
| **Priority Queue** | O(log n) | O(log n) | Dynamic | Elements by priority | More complex |
| **Deque** | O(1) | O(1) | Dynamic | Operations at both ends | More memory overhead |

## When to Use Each Type

**Linked List Queue**: Best for general-purpose queuing when you don't know the maximum size and need simple FIFO behavior.

**Circular Array Queue**: Ideal when you know the maximum capacity and want memory efficiency.

**Priority Queue**: Use when elements have different priorities and should be processed based on importance rather than arrival order.

**Deque**: Perfect when you need to add/remove elements from both ends, like implementing undo/redo functionality.

## Real-World Applications

**Task Scheduling**: Operating systems use queues to manage process scheduling and task execution.

**BFS Algorithm**: Graph traversal algorithms use queues to explore nodes level by level.

**Print Queues**: Printers use queues to manage multiple print jobs in order.

**Web Servers**: Handle incoming requests in the order they arrive.

**Breadth-First Search**: Used in pathfinding, social networks, and web crawling.

The choice of queue implementation depends on your specific needs regarding capacity, performance requirements, and the types of operations you'll perform most frequently.