# Circular LinkedList Complete Guide & Python Implementation

## 🔄 What is a Circular LinkedList?

A **Circular LinkedList** is a variation of linked lists where:
- The **last node** points back to the **first node** instead of NULL
- Creates a **circular chain** with no definitive end
- Can be **singly circular** or **doubly circular**

## 🔗 Types of Circular LinkedLists

### 1. Singly Circular LinkedList
```
[1] -> [2] -> [3] -> [4] ┐
 ↑                      │
 └──────────────────────┘
```

### 2. Doubly Circular LinkedList
```
    ┌─────────────────────┐
    ↓                     │
[1] ⟷ [2] ⟷ [3] ⟷ [4] ──┘
 ↑                     
 └─────────────────────
```

## 📊 Circular vs Linear LinkedList

| Feature | Linear LinkedList | Circular LinkedList |
|---------|-------------------|-------------------|
| Last node points to | NULL | First node |
| Traversal | Has definite end | Can loop infinitely |
| Memory access | Sequential | Cyclic |
| Applications | General purpose | Round-robin, games |
| Boundary detection | Check for NULL | Check for head |

## 🎯 Advantages of Circular LinkedLists

1. **No NULL pointers** - Every node points to something
2. **Efficient round-robin** - Perfect for scheduling algorithms
3. **Constant access** - Can start from any node
4. **Memory efficient** - No wasted NULL pointers
5. **Natural cycles** - Great for cyclical processes

## ⚠️ Challenges

1. **Infinite loops** - Easy to create accidental infinite loops
2. **Termination condition** - Need to track when to stop
3. **Memory leaks** - Circular references can cause GC issues
4. **Complexity** - More complex insertion/deletion logic

## 🐍 Singly Circular LinkedList Implementation

```python
class Node:
    """Node class for singly circular linked list"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class SinglyCircularLinkedList:
    """Singly Circular LinkedList implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None
    
    def get_size(self):
        """Get size of the list - O(1)"""
        return self.size
    
    def prepend(self, data):
        """Add element at the beginning - O(n)"""
        new_node = Node(data)
        
        if self.is_empty():
            # First node points to itself
            new_node.next = new_node
            self.head = new_node
        else:
            # Find the last node (points to current head)
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Connect new node
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
        
        self.size += 1
    
    def append(self, data):
        """Add element at the end - O(n)"""
        new_node = Node(data)
        
        if self.is_empty():
            # First node points to itself
            new_node.next = new_node
            self.head = new_node
        else:
            # Find the last node
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Connect new node
            new_node.next = self.head
            last.next = new_node
        
        self.size += 1
    
    def insert_at(self, index, data):
        """Insert element at specific index - O(n)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        # Traverse to the position
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_first(self):
        """Delete first element - O(n)"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        deleted_data = self.head.data
        
        if self.size == 1:
            # Only one node
            self.head = None
        else:
            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next
            
            # Update connections
            last.next = self.head.next
            self.head = self.head.next
        
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete last element - O(n)"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        if self.size == 1:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        # Find second to last node
        current = self.head
        while current.next.next != self.head:
            current = current.next
        
        deleted_data = current.next.data
        current.next = self.head
        self.size -= 1
        return deleted_data
    
    def delete_at(self, index):
        """Delete element at specific index - O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            return self.delete_first()
        
        current = self.head
        for i in range(index - 1):
            current = current.next
        
        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data
    
    def find(self, data):
        """Find element and return index - O(n)"""
        if self.is_empty():
            return -1
        
        current = self.head
        index = 0
        
        # Check first node
        if current.data == data:
            return index
        
        current = current.next
        index += 1
        
        # Traverse the rest
        while current != self.head:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1  # Not found
    
    def get(self, index):
        """Get element at specific index - O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for i in range(index):
            current = current.next
        
        return current.data
    
    def display(self):
        """Display all elements - O(n)"""
        if self.is_empty():
            return "Empty circular list"
        
        elements = []
        current = self.head
        
        # Add first element
        elements.append(str(current.data))
        current = current.next
        
        # Add remaining elements
        while current != self.head:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements) + " -> (back to " + str(self.head.data) + ")"
    
    def display_n_rounds(self, rounds=2):
        """Display list for n complete rounds - useful for visualization"""
        if self.is_empty():
            return "Empty circular list"
        
        elements = []
        current = self.head
        total_elements = rounds * self.size
        
        for i in range(total_elements):
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements) + " -> ..."
    
    def to_list(self):
        """Convert to Python list - O(n)"""
        if self.is_empty():
            return []
        
        result = []
        current = self.head
        
        # Add first element
        result.append(current.data)
        current = current.next
        
        # Add remaining elements
        while current != self.head:
            result.append(current.data)
            current = current.next
        
        return result
    
    def __len__(self):
        """Support for len() function - O(1)"""
        return self.size
    
    def __str__(self):
        """String representation"""
        return self.display()
    
    def __iter__(self):
        """Make the list iterable (one complete round)"""
        if self.is_empty():
            return
        
        current = self.head
        yield current.data
        current = current.next
        
        while current != self.head:
            yield current.data
            current = current.next

# Doubly Circular LinkedList Implementation
class DoublyNode:
    """Node class for doubly circular linked list"""
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return str(self.data)

class DoublyCircularLinkedList:
    """Doubly Circular LinkedList implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None
    
    def get_size(self):
        """Get size of the list - O(1)"""
        return self.size
    
    def prepend(self, data):
        """Add element at the beginning - O(1)"""
        new_node = DoublyNode(data)
        
        if self.is_empty():
            # First node points to itself in both directions
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            # Get the tail (previous to head)
            tail = self.head.prev
            
            # Connect new node
            new_node.next = self.head
            new_node.prev = tail
            
            # Update existing connections
            self.head.prev = new_node
            tail.next = new_node
            
            # Update head
            self.head = new_node
        
        self.size += 1
    
    def append(self, data):
        """Add element at the end - O(1)"""
        new_node = DoublyNode(data)
        
        if self.is_empty():
            # First node points to itself in both directions
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            # Get the tail (previous to head)
            tail = self.head.prev
            
            # Connect new node
            new_node.next = self.head
            new_node.prev = tail
            
            # Update existing connections
            tail.next = new_node
            self.head.prev = new_node
        
        self.size += 1
    
    def insert_at(self, index, data):
        """Insert element at specific index - O(n)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(data)
            return
        
        if index == self.size:
            self.append(data)
            return
        
        # Find the node at index
        current = self.head
        for i in range(index):
            current = current.next
        
        # Create and connect new node
        new_node = DoublyNode(data)
        new_node.next = current
        new_node.prev = current.prev
        
        # Update existing connections
        current.prev.next = new_node
        current.prev = new_node
        
        self.size += 1
    
    def delete_first(self):
        """Delete first element - O(1)"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        deleted_data = self.head.data
        
        if self.size == 1:
            # Only one node
            self.head = None
        else:
            # Get tail
            tail = self.head.prev
            new_head = self.head.next
            
            # Update connections
            tail.next = new_head
            new_head.prev = tail
            
            # Update head
            self.head = new_head
        
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete last element - O(1)"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        if self.size == 1:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        # Get tail and new tail
        tail = self.head.prev
        new_tail = tail.prev
        
        deleted_data = tail.data
        
        # Update connections
        new_tail.next = self.head
        self.head.prev = new_tail
        
        self.size -= 1
        return deleted_data
    
    def delete_at(self, index):
        """Delete element at specific index - O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            return self.delete_first()
        
        if index == self.size - 1:
            return self.delete_last()
        
        # Find node to delete
        current = self.head
        for i in range(index):
            current = current.next
        
        deleted_data = current.data
        
        # Update connections
        current.prev.next = current.next
        current.next.prev = current.prev
        
        self.size -= 1
        return deleted_data
    
    def find(self, data):
        """Find element and return index - O(n)"""
        if self.is_empty():
            return -1
        
        current = self.head
        for i in range(self.size):
            if current.data == data:
                return i
            current = current.next
        
        return -1  # Not found
    
    def get(self, index):
        """Get element at specific index - O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        current = self.head
        for i in range(index):
            current = current.next
        
        return current.data
    
    def display_forward(self):
        """Display all elements forward - O(n)"""
        if self.is_empty():
            return "Empty circular list"
        
        elements = []
        current = self.head
        
        for i in range(self.size):
            elements.append(str(current.data))
            current = current.next
        
        return " <-> ".join(elements) + " <-> (circular)"
    
    def display_backward(self):
        """Display all elements backward - O(n)"""
        if self.is_empty():
            return "Empty circular list"
        
        elements = []
        current = self.head.prev  # Start from tail
        
        for i in range(self.size):
            elements.append(str(current.data))
            current = current.prev
        
        return " <-> ".join(elements) + " <-> (circular)"
    
    def to_list_forward(self):
        """Convert to Python list (forward) - O(n)"""
        if self.is_empty():
            return []
        
        result = []
        current = self.head
        for i in range(self.size):
            result.append(current.data)
            current = current.next
        
        return result
    
    def to_list_backward(self):
        """Convert to Python list (backward) - O(n)"""
        if self.is_empty():
            return []
        
        result = []
        current = self.head.prev  # Start from tail
        for i in range(self.size):
            result.append(current.data)
            current = current.prev
        
        return result
    
    def __len__(self):
        """Support for len() function - O(1)"""
        return self.size
    
    def __str__(self):
        """String representation"""
        return self.display_forward()
    
    def __iter__(self):
        """Make the list iterable (forward, one complete round)"""
        if self.is_empty():
            return
        
        current = self.head
        for i in range(self.size):
            yield current.data
            current = current.next

# Example Usage and Testing
if __name__ == "__main__":
    print("=== Singly Circular LinkedList Demo ===")
    
    # Create singly circular list
    scl = SinglyCircularLinkedList()
    
    # Add elements
    scl.append(1)
    scl.append(2)
    scl.append(3)
    scl.prepend(0)
    
    print(f"Singly circular list: {scl}")
    print(f"Two rounds: {scl.display_n_rounds(2)}")
    print(f"Size: {len(scl)}")
    
    # Test operations
    print(f"Element at index 2: {scl.get(2)}")
    print(f"Index of element 2: {scl.find(2)}")
    
    scl.insert_at(2, 1.5)
    print(f"After inserting 1.5 at index 2: {scl}")
    
    deleted = scl.delete_at(1)
    print(f"Deleted element {deleted}: {scl}")
    
    print("\n=== Doubly Circular LinkedList Demo ===")
    
    # Create doubly circular list
    dcl = DoublyCircularLinkedList()
    
    # Add elements
    dcl.append(10)
    dcl.append(20)
    dcl.append(30)
    dcl.prepend(5)
    
    print(f"Doubly circular list: {dcl}")
    print(f"Forward: {dcl.display_forward()}")
    print(f"Backward: {dcl.display_backward()}")
    print(f"Size: {len(dcl)}")
    
    # Test bidirectional operations
    dcl.insert_at(2, 15)
    print(f"After inserting 15 at index 2: {dcl}")
    
    print(f"Deleted first: {dcl.delete_first()}")
    print(f"Deleted last: {dcl.delete_last()}")
    print(f"Final list: {dcl}")
    
    # Demonstrate iteration
    print("\nIterating through doubly circular list:")
    for item in dcl:
        print(f"  {item}")
```

## 🔧 Specialized Circular LinkedList Operations

### 1. **Josephus Problem Solution**
```python
def josephus_problem(n, k):
    """Solve Josephus problem using circular linked list"""
    # Create circular list with n people
    people = SinglyCircularLinkedList()
    for i in range(1, n + 1):
        people.append(i)
    
    # Start elimination
    current = people.head
    while people.size > 1:
        # Count k-1 steps
        for _ in range(k - 1):
            prev = current
            current = current.next
        
        # Eliminate current person
        if current == people.head:
            people.delete_first()
            current = people.head
        else:
            prev.next = current.next
            current = current.next
            people.size -= 1
    
    return people.head.data
```

### 2. **Round Robin Scheduler**
```python
class RoundRobinScheduler:
    """Round robin scheduler using circular linked list"""
    
    def __init__(self):
        self.processes = DoublyCircularLinkedList()
        self.current = None
    
    def add_process(self, process_id):
        """Add a process to the scheduler"""
        self.processes.append(process_id)
        if self.current is None:
            self.current = self.processes.head
    
    def get_next_process(self):
        """Get next process in round robin fashion"""
        if self.current is None:
            return None
        
        process = self.current.data
        self.current = self.current.next
        return process
    
    def remove_process(self, process_id):
        """Remove a process from scheduler"""
        index = self.processes.find(process_id)
        if index != -1:
            # Update current pointer if needed
            if self.processes.size == 1:
                self.current = None
            elif self.current.data == process_id:
                self.current = self.current.next
            
            self.processes.delete_at(index)
```

### 3. **Circular Buffer Implementation**
```python
class CircularBuffer:
    """Circular buffer using circular linked list"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = SinglyCircularLinkedList()
        self.write_pos = None
        self.read_pos = None
    
    def write(self, data):
        """Write data to buffer"""
        if self.buffer.size < self.capacity:
            self.buffer.append(data)
            if self.write_pos is None:
                self.write_pos = self.buffer.head
                self.read_pos = self.buffer.head
            else:
                # Move write position
                current = self.buffer.head
                while current.next != self.buffer.head:
                    current = current.next
                self.write_pos = current
        else:
            # Overwrite oldest data
            self.write_pos.data = data
            self.write_pos = self.write_pos.next
            self.read_pos = self.read_pos.next  # Move read pos too
    
    def read(self):
        """Read data from buffer"""
        if self.buffer.is_empty():
            return None
        
        data = self.read_pos.data
        self.read_pos = self.read_pos.next
        return data
```

## 🚀 Advanced Circular LinkedList Algorithms

### 1. **Split Circular List**
```python
def split_circular_list(head):
    """Split circular list into two halves"""
    if not head or head.next == head:
        return head, None
    
    # Find middle using slow/fast pointers
    slow = fast = head
    prev_slow = None
    
    while fast.next != head and fast.next.next != head:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    
    # If even number of nodes
    if fast.next.next == head:
        fast = fast.next
    
    # Split the lists
    head2 = slow.next
    fast.next = head2  # Complete second circle
    prev_slow.next = head  # Complete first circle
    
    return head, head2
```

### 2. **Check if LinkedList is Circular**
```python
def is_circular(head):
    """Check if a linked list is circular using Floyd's algorithm"""
    if not head:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            # Found cycle, check if it includes head
            temp = head
            while temp.next != head and temp.next != slow:
                temp = temp.next
            
            return temp.next == head
    
    return False
```

### 3. **Convert Linear to Circular**
```python
def convert_to_circular(head):
    """Convert linear linked list to circular"""
    if not head:
        return head
    
    current = head
    while current.next:
        current = current.next
    
    # Connect last node to first
    current.next = head
    return head
```

## ⚡ Performance Comparison

| Operation | Singly Linear | Singly Circular | Doubly Circular |
|-----------|---------------|-----------------|-----------------|
| Insert at start | O(1) | O(n)* | O(1) |
| Insert at end | O(n) | O(n) | O(1) |
| Delete at start | O(1) | O(n)* | O(1) |
| Delete at end | O(n) | O(n) | O(1) |
| Access by index | O(n) | O(n) | O(n) |
| Search | O(n) | O(n) | O(n) |

*O(n) because we need to find the last node to update its pointer

## 🧠 Common Interview Problems

### 1. **Find Loop Start in Circular List**
```python
def find_loop_start(head):
    """Find where the loop starts in a circular list"""
    # Use Floyd's cycle detection
    slow = fast = head
    
    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    # Move one pointer to head, keep other at meeting point
    ptr1 = head
    ptr2 = slow
    
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1  # Loop start
```

### 2. **Clone Circular List with Random Pointers**
```python
def clone_circular_list_with_random(head):
    """Clone circular list where each node has random pointer"""
    if not head:
        return None
    
    # Step 1: Create cloned nodes
    current = head
    node_map = {}
    
    # First pass: create all nodes
    temp = current
    while True:
        node_map[temp] = DoublyNode(temp.data)
        temp = temp.next
        if temp == head:
            break
    
    # Second pass: connect pointers
    temp = current
    while True:
        cloned = node_map[temp]
        cloned.next = node_map[temp.next]
        cloned.prev = node_map[temp.prev]
        if hasattr(temp, 'random') and temp.random:
            cloned.random = node_map[temp.random]
        
        temp = temp.next
        if temp == head:
            break
    
    return node_map[head]
```

## 💡 Real-World Applications

### 1. **Operating Systems**
- **CPU Scheduling**: Round-robin scheduling
- **Buffer Management**: Circular buffers
- **Process Queues**: Fair resource allocation

### 2. **Gaming**
- **Turn-based Games**: Player rotation
- **Playlist Management**: Continuous music play
- **Animation Loops**: Cycling through frames

### 3. **Embedded Systems**
- **Sensor Data**: Continuous monitoring
- **Real-time Processing**: Circular queues
- **Memory Management**: Ring buffers

### 4. **Network Programming**
- **Load Balancing**: Server rotation
- **Token Ring Networks**: Data transmission
- **Buffering**: Network packet management

## 🏆 Practice Problems

1. **Josephus Problem** - Classic elimination game
2. **Split Circular List** - Divide into two circular lists
3. **Merge Circular Lists** - Combine two circular lists
4. **Check Palindrome** - In circular doubly linked list
5. **Sort Circular List** - Maintain circular property
6. **LRU Cache with Circular List** - Efficient cache implementation
7. **Music Player** - Playlist with repeat functionality
8. **Circular Tour** - Find starting point for circular journey

## 🎯 Key Takeaways

### ✅ When to Use Circular LinkedLists:
- **Round-robin operations** (scheduling, games)
- **Continuous cycles** (playlists, animations)
- **Fixed-size buffers** (circular queues)
- **No natural end point** (circular processes)

### ⚠️ When to Avoid:
- **Simple sequential access** (use linear lists)
- **Frequent random access** (use arrays)
- **Memory-critical applications** (extra complexity overhead)
- **When NULL termination is important**

### 🔑 Critical Points:
1. **Always track size** - Prevent infinite loops
2. **Careful with termination conditions** - Don't use NULL checks
3. **Initialize properly** - Single node points to itself
4. **Handle edge cases** - Empty list, single node
5. **Memory management** - Be aware of circular references

Circular linked lists are powerful for specific use cases but require careful handling. Master the circular thinking, and you'll have a valuable tool for cyclical algorithms and round-robin operations!