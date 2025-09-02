# Doubly LinkedList Complete Guide & Python Implementation

## 🔗 What is a Doubly LinkedList?

A **Doubly LinkedList** is a linear data structure where each node contains:
- **Data**: The actual value stored
- **Next pointer**: Reference to the next node
- **Previous pointer**: Reference to the previous node

This bidirectional linking allows traversal in both directions!

## 📊 Doubly vs Singly LinkedList

| Feature | Singly LinkedList | Doubly LinkedList |
|---------|-------------------|-------------------|
| Pointers per node | 1 (next) | 2 (next + prev) |
| Memory per node | Less | More |
| Traversal | Forward only | Both directions |
| Deletion with node ref | O(n) | O(1) |
| Implementation complexity | Simpler | More complex |

## 🎯 Key Advantages of Doubly LinkedList

1. **Bidirectional traversal** - Can go forward and backward
2. **Efficient deletion** - O(1) if you have node reference
3. **Better for certain algorithms** - Like LRU cache implementation
4. **No need to track previous node** - During traversal for deletions

## 🐍 Complete Python Implementation

```python
class Node:
    """Node class for doubly linked list"""
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    """Doubly LinkedList implementation with head and tail pointers"""
    
    def __init__(self):
        self.head = None
        self.tail = None  # Track tail for O(1) append
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None
    
    def get_size(self):
        """Get size of the list - O(1)"""
        return self.size
    
    def prepend(self, data):
        """Add element at the beginning - O(1)"""
        new_node = Node(data)
        
        if self.is_empty():
            # First node becomes both head and tail
            self.head = self.tail = new_node
        else:
            # Connect new node to current head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def append(self, data):
        """Add element at the end - O(1)"""
        new_node = Node(data)
        
        if self.is_empty():
            # First node becomes both head and tail
            self.head = self.tail = new_node
        else:
            # Connect new node to current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
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
        
        # Choose optimal traversal direction
        if index <= self.size // 2:
            # Traverse from head
            current = self.head
            for i in range(index):
                current = current.next
        else:
            # Traverse from tail (optimization!)
            current = self.tail
            for i in range(self.size - index - 1):
                current = current.prev
        
        # Insert before current node
        new_node = Node(data)
        new_node.prev = current.prev
        new_node.next = current
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
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete last element - O(1)"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        deleted_data = self.tail.data
        
        if self.size == 1:
            # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
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
        
        # Choose optimal traversal direction
        if index <= self.size // 2:
            # Traverse from head
            current = self.head
            for i in range(index):
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for i in range(self.size - index - 1):
                current = current.prev
        
        # Remove current node
        deleted_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        
        self.size -= 1
        return deleted_data
    
    def delete_node(self, node):
        """Delete specific node - O(1) if you have node reference!"""
        if not node:
            return
        
        # Handle head deletion
        if node == self.head:
            return self.delete_first()
        
        # Handle tail deletion
        if node == self.tail:
            return self.delete_last()
        
        # Delete middle node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.data
    
    def find(self, data):
        """Find element and return index - O(n)"""
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1  # Not found
    
    def find_node(self, data):
        """Find and return the actual node - O(n)"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def get(self, index):
        """Get element at specific index - O(n), optimized for direction"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Choose optimal traversal direction
        if index <= self.size // 2:
            # Traverse from head
            current = self.head
            for i in range(index):
                current = current.next
        else:
            # Traverse from tailre
            current = self.tail
            for i in range(self.size - index - 1):
                current = current.prev
        
        return current.data
    
    def reverse(self):
        """Reverse the linked list - O(n)"""
        current = self.head
        
        # Swap head and tail
        self.head, self.tail = self.tail, self.head
        
        # Swap next and prev for each node
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev  # Note: moving to prev (which was next)
    
    def display_forward(self):
        """Display all elements from head to tail - O(n)"""
        if self.is_empty():
            return "Empty list"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return "None <- " + " <-> ".join(elements) + " -> None"
    
    def display_backward(self):
        """Display all elements from tail to head - O(n)"""
        if self.is_empty():
            return "Empty list"
        
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        
        return "None <- " + " <-> ".join(elements) + " -> None"
    
    def to_list_forward(self):
        """Convert to Python list (forward) - O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def to_list_backward(self):
        """Convert to Python list (backward) - O(n)"""
        result = []
        current = self.tail
        while current:
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
        """Make the list iterable (forward direction)"""
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def iter_backward(self):
        """Iterate in reverse direction"""
        current = self.tail
        while current:
            yield current.data
            current = current.prev

# Example Usage and Testing
if __name__ == "__main__":
    print("=== Doubly LinkedList Operations Demo ===")
    
    # Create a new doubly linked list
    dll = DoublyLinkedList()
    
    # Test basic operations
    print(f"Initial list: {dll}")
    print(f"Is empty: {dll.is_empty()}")
    
    # Add elements
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(f"After appending 1,2,3: {dll}")
    
    dll.prepend(0)
    print(f"After prepending 0: {dll}")
    
    # Insert at specific position
    dll.insert_at(2, 1.5)
    print(f"After inserting 1.5 at index 2: {dll}")
    
    # Show bidirectional capability
    print(f"Forward:  {dll.display_forward()}")
    print(f"Backward: {dll.display_backward()}")
    
    # Access elements
    print(f"Element at index 0: {dll.get(0)}")
    print(f"Element at index 2: {dll.get(2)}")
    print(f"Element at index 4: {dll.get(4)}")
    
    # Search for elements
    print(f"Index of element 2: {dll.find(2)}")
    print(f"Index of element 5: {dll.find(5)}")
    
    # Delete operations
    print(f"Deleted first element: {dll.delete_first()}")
    print(f"After deletion: {dll}")
    
    print(f"Deleted last element: {dll.delete_last()}")
    print(f"After deletion: {dll}")
    
    print(f"Deleted element at index 1: {dll.delete_at(1)}")
    print(f"After deletion: {dll}")
    
    # Test node-specific deletion
    node_to_delete = dll.find_node(2)
    if node_to_delete:
        dll.delete_node(node_to_delete)
        print(f"After deleting node with value 2: {dll}")
    
    # Reverse the list
    dll.reverse()
    print(f"After reversing: {dll}")
    
    # List properties
    print(f"Size: {len(dll)}")
    print(f"Forward list: {dll.to_list_forward()}")
    print(f"Backward list: {dll.to_list_backward()}")
    
    # Demonstrate bidirectional iteration
    print("Forward iteration:")
    for item in dll:
        print(f"  {item}")
    
    print("Backward iteration:")
    for item in dll.iter_backward():
        print(f"  {item}")
```

## 🔑 Key Concepts for Doubly LinkedLists

### 1. **Always Update Both Directions**
```python
# When connecting nodes, update BOTH pointers:
node1.next = node2
node2.prev = node1
```

### 2. **Track Both Head AND Tail**
- Head: For forward operations and traversal
- Tail: For backward operations and O(1) append

### 3. **Handle Edge Cases**
- Empty list
- Single node (head == tail)
- First/last node operations

### 4. **Optimization: Choose Traversal Direction**
```python
# Smart traversal: choose closer end
if index <= size // 2:
    traverse_from_head()
else:
    traverse_from_tail()
```

## 🚀 Unique Doubly LinkedList Operations

### 1. **O(1) Node Deletion**
```python
def delete_node(self, node):
    """Delete specific node in O(1) time!"""
    # This is impossible in singly linked lists
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev
```

### 2. **Bidirectional Traversal**
```python
# Forward
current = head
while current:
    current = current.next

# Backward  
current = tail
while current:
    current = current.prev
```

## 🔧 Common Patterns & Algorithms

### 1. **LRU Cache Implementation**
Doubly linked lists are perfect for LRU (Least Recently Used) caches:
```python
def move_to_front(self, node):
    """Move node to front (most recently used)"""
    if node == self.head:
        return
    
    # Remove from current position
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev
    if node == self.tail:
        self.tail = node.prev
    
    # Add to front
    node.prev = None
    node.next = self.head
    self.head.prev = node
    self.head = node
```

### 2. **Palindrome Check**
```python
def is_palindrome(self):
    """Check if list is palindrome using two pointers"""
    if self.size <= 1:
        return True
    
    left = self.head
    right = self.tail
    
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
    
    return True
```

### 3. **Merge Two Sorted Lists**
```python
def merge_sorted(list1, list2):
    """Merge two sorted doubly linked lists"""
    dummy = Node(0)
    current = dummy
    
    ptr1, ptr2 = list1.head, list2.head
    
    while ptr1 and ptr2:
        if ptr1.data <= ptr2.data:
            current.next = ptr1
            ptr1.prev = current
            ptr1 = ptr1.next
        else:
            current.next = ptr2
            ptr2.prev = current
            ptr2 = ptr2.next
        current = current.next
    
    # Attach remaining nodes
    remaining = ptr1 or ptr2
    if remaining:
        current.next = remaining
        remaining.prev = current
    
    # Create new list with merged nodes
    result = DoublyLinkedList()
    if dummy.next:
        result.head = dummy.next
        result.head.prev = None
        
        # Find tail
        current = result.head
        while current.next:
            current = current.next
            result.size += 1
        result.tail = current
        result.size += 1
    
    return result
```

## ⚡ Performance Analysis

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Access by index | O(n) | Can optimize by choosing direction |
| Search | O(n) | Same as singly linked |
| Insert at beginning | O(1) | With head pointer |
| Insert at end | O(1) | With tail pointer |
| Insert at middle | O(n) | Need to traverse |
| Delete with node ref | O(1) | **Big advantage over singly!** |
| Delete by index | O(n) | Can optimize direction |
| Reverse | O(n) | Just swap pointers |

## 🧠 Interview Questions & Solutions

### 1. **Remove Duplicates**
```python
def remove_duplicates(self):
    """Remove duplicates from sorted doubly linked list"""
    if self.is_empty():
        return
    
    current = self.head
    while current and current.next:
        if current.data == current.next.data:
            # Delete duplicate
            duplicate = current.next
            current.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = current
            else:
                self.tail = current  # Update tail if needed
            self.size -= 1
        else:
            current = current.next
```

### 2. **Find Pairs with Given Sum**
```python
def find_pair_with_sum(self, target):
    """Find pair of nodes that sum to target"""
    if self.size < 2:
        return None
    
    left = self.head
    right = self.tail
    
    while left != right and left.prev != right:
        current_sum = left.data + right.data
        
        if current_sum == target:
            return (left.data, right.data)
        elif current_sum < target:
            left = left.next
        else:
            right = right.prev
    
    return None
```

### 3. **Rotate List**
```python
def rotate_right(self, k):
    """Rotate list to the right by k positions"""
    if self.is_empty() or k == 0:
        return
    
    k = k % self.size  # Handle k > size
    if k == 0:
        return
    
    # Find the new tail (size - k - 1 from head)
    new_tail = self.head
    for i in range(self.size - k - 1):
        new_tail = new_tail.next
    
    # New head is next to new tail
    new_head = new_tail.next
    
    # Break the connection
    new_tail.next = None
    new_head.prev = None
    
    # Connect old tail to old head
    self.tail.next = self.head
    self.head.prev = self.tail
    
    # Update head and tail
    self.head = new_head
    self.tail = new_tail
```

## 🔍 Debugging Tips

### 1. **Pointer Integrity Check**
```python
def validate_integrity(self):
    """Debug method to check if all pointers are correct"""
    if self.is_empty():
        return True
    
    # Check head
    if self.head.prev is not None:
        return False
    
    # Check tail
    if self.tail.next is not None:
        return False
    
    # Check all connections
    current = self.head
    count = 0
    while current:
        count += 1
        if current.next:
            if current.next.prev != current:
                return False
        current = current.next
    
    return count == self.size
```

### 2. **Visualization Helper**
```python
def visualize(self):
    """Visual representation showing all pointers"""
    if self.is_empty():
        return "Empty list"
    
    result = []
    current = self.head
    
    while current:
        prev_data = current.prev.data if current.prev else "None"
        next_data = current.next.data if current.next else "None"
        
        result.append(f"[{prev_data}|{current.data}|{next_data}]")
        current = current.next
    
    return " <-> ".join(result)
```

## 💡 Real-World Applications

1. **Browser History** - Forward/back navigation
2. **Music Playlist** - Previous/next song
3. **Undo/Redo Systems** - Text editors
4. **LRU Cache** - Operating systems
5. **Deque Implementation** - Double-ended queue

## 🏆 Practice Problems

1. **Design Browser History** - Implement back/forward functionality
2. **LRU Cache** - Use doubly linked list + hashmap
3. **Flatten Multilevel List** - Handle child pointers
4. **Copy List with Random Pointer** - Deep copy with extra pointers
5. **Sort Doubly LinkedList** - Implement merge sort
6. **Find Critical Connections** - Graph theory application

## 🎯 Key Takeaways

1. **Memory Trade-off**: Extra pointer per node for bidirectional capability
2. **O(1) Node Deletion**: Major advantage when you have node reference
3. **Direction Optimization**: Choose head/tail traversal based on index
4. **Tail Pointer**: Essential for O(1) append operations
5. **Edge Cases**: Always handle empty, single node, head/tail scenarios
6. **Pointer Integrity**: Both directions must stay consistent

The doubly linked list offers more flexibility than singly linked lists at the cost of extra memory and complexity. Master the bidirectional pointer management, and you'll have a powerful tool for many algorithmic problems!