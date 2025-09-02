# LinkedList Cheat Sheet & Python Implementation

## 📋 LinkedList Overview

A **LinkedList** is a linear data structure where elements (nodes) are stored in sequence, but not in contiguous memory locations. Each node contains data and a reference (pointer) to the next node.

## 🔗 Types of LinkedLists

### 1. Singly LinkedList
- Each node points to the next node
- Traversal: Only forward direction
- Memory: Less memory per node

### 2. Doubly LinkedList
- Each node has pointers to both next and previous nodes
- Traversal: Both forward and backward
- Memory: More memory per node

### 3. Circular LinkedList
- Last node points back to the first node
- Can be singly or doubly linked
- No null pointers at the end

## ⚡ Time Complexities

| Operation | Array | LinkedList |
|-----------|-------|------------|
| Access    | O(1)  | O(n)       |
| Search    | O(n)  | O(n)       |
| Insertion | O(n)  | O(1)*      |
| Deletion  | O(n)  | O(1)*      |

*O(1) if you have reference to the node, O(n) if searching first

## 🎯 When to Use LinkedLists

### ✅ Advantages
- Dynamic size (grows/shrinks during runtime)
- Efficient insertion/deletion at beginning
- Memory allocated as needed
- Good for implementing stacks, queues

### ❌ Disadvantages
- No random access (must traverse from head)
- Extra memory for storing pointers
- Not cache-friendly
- No backward traversal (singly linked)

## 🐍 Python Implementation - Singly LinkedList

```python
class ListNode:
    """Node class for singly linked list"""
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    """Singly LinkedList implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty"""
        return self.head is None
    
    def get_size(self):
        """Get size of the list"""
        return self.size
    
    def prepend(self, data):
        """Add element at the beginning - O(1)"""
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def append(self, data):
        """Add element at the end - O(n)"""
        new_node = ListNode(data)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def insert_at(self, index, data):
        """Insert element at specific index - O(n)"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = ListNode(data)
        current = self.head
        
        for i in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_first(self):
        """Delete first element - O(1)"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data
    
    def delete_last(self):
        """Delete last element - O(n)"""
        if self.is_empty():
            raise ValueError("List is empty")
        
        if self.head.next is None:  # Only one element
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        deleted_data = current.next.data
        current.next = None
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
        current = self.head
        index = 0
        
        while current:
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
    
    def reverse(self):
        """Reverse the linked list - O(n)"""
        prev = None
        current = self.head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        self.head = prev
    
    def display(self):
        """Display all elements - O(n)"""
        if self.is_empty():
            return "Empty list"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements) + " -> None"
    
    def to_list(self):
        """Convert to Python list - O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self):
        """Support for len() function"""
        return self.size
    
    def __str__(self):
        """String representation"""
        return self.display()
    
    def __iter__(self):
        """Make the list iterable"""
        current = self.head
        while current:
            yield current.data
            current = current.next

# Example Usage and Testing
if __name__ == "__main__":
    # Create a new linked list
    ll = SinglyLinkedList()
    
    # Test basic operations
    print("=== LinkedList Operations Demo ===")
    
    # Add elements
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print(f"After adding 0,1,2,3: {ll}")
    
    # Insert at specific position
    ll.insert_at(2, 1.5)
    print(f"After inserting 1.5 at index 2: {ll}")
    
    # Access elements
    print(f"Element at index 0: {ll.get(0)}")
    print(f"Element at index 2: {ll.get(2)}")
    
    # Search for elements
    print(f"Index of element 2: {ll.find(2)}")
    print(f"Index of element 5: {ll.find(5)}")
    
    # Delete operations
    print(f"Deleted first element: {ll.delete_first()}")
    print(f"After deletion: {ll}")
    
    print(f"Deleted element at index 1: {ll.delete_at(1)}")
    print(f"After deletion: {ll}")
    
    # Reverse the list
    ll.reverse()
    print(f"After reversing: {ll}")
    
    # List properties
    print(f"Size: {len(ll)}")
    print(f"Is empty: {ll.is_empty()}")
    
    # Convert to Python list
    print(f"As Python list: {ll.to_list()}")
    
    # Iterate through list
    print("Iterating through list:")
    for item in ll:
        print(f"  {item}")
```

## 🔧 Common LinkedList Patterns

### 1. Two Pointers Technique
```python
def find_middle(head):
    """Find middle node using slow/fast pointers"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### 2. Cycle Detection (Floyd's Algorithm)
```python
def has_cycle(head):
    """Detect cycle using slow/fast pointers"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### 3. Merge Two Sorted Lists
```python
def merge_sorted_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    current.next = l1 or l2
    return dummy.next
```

## 🧠 Interview Tips

### Common Questions
1. **Reverse a LinkedList** - Practice iterative and recursive approaches
2. **Detect cycles** - Use Floyd's cycle detection
3. **Find nth node from end** - Two pointers with n gap
4. **Merge sorted lists** - Use dummy node technique
5. **Remove duplicates** - Track previous node
6. **Check palindrome** - Reverse second half and compare

### Key Points to Remember
- Always check for null/empty cases
- Be careful with pointer manipulation
- Consider edge cases (single node, empty list)
- Think about whether you need to track previous node
- Dummy nodes can simplify insertion/deletion logic

## 🔄 LinkedList vs Array

| Aspect | Array | LinkedList |
|--------|-------|------------|
| Memory | Contiguous | Scattered |
| Cache Performance | Better | Worse |
| Random Access | Yes | No |
| Dynamic Size | No* | Yes |
| Memory Overhead | Lower | Higher |
| Insertion/Deletion | Expensive | Cheap |

*Dynamic arrays like Python lists can resize, but with O(n) cost occasionally

## 💡 Practice Problems

1. Reverse a linked list (iteratively and recursively)
2. Find the middle of a linked list
3. Detect if a linked list has a cycle
4. Remove nth node from end
5. Merge two sorted linked lists
6. Remove duplicates from sorted list
7. Check if linked list is palindrome
8. Find intersection point of two linked lists