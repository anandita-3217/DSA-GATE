class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data 
        self.prev = prev
        self.next = next
    def __str__(self):
        return str(self.data)
"""
A doubly linked list is a more complex data structure than a singly linked list, but it offers several advantages. 
The main advantage of a doubly linked list is that it allows for efficient traversal of the list in both directions. 
This is because each node in the list contains a pointer to the previous node and a pointer to the next node. 
This allows for quick and easy insertion and deletion of nodes from the list, as well as efficient traversal of the list in both directions.


"""
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None # Track tail for O(1) append
        self.size = 0
    
    def is_empty(self):
        # Check if Linked List is Empty
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def prepend(self,data):
        """Add element at the beginning - O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def delete_first(self):
        """Delete first node"""
        if self.is_empty():
            raise ValueError("Linked List is Empty")
        deleted_data = self.head.data
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return deleted_data



    def append(self, data):
        """Add at end - O(1) with tail pointer, O(n) without"""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_last(self):
        """Delete last node"""
        if self.is_empty():
            raise ValueError("Linked List is Empty")
        deleted_data = self.tail.data
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return deleted_data
    
    def insert_at(self, index, data):
        """Insert at specific index"""
        if index < 0 or index > self.size:
            raise IndexError("index Out of Bounds")
        
        if index == 0:
            self.prepend(data)
            return 
        if index == self.size:
            self.append(data)
            return
        if index <= self.size // 2:
            current = self.head
            for i in range(index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.size - index - 1):
                current = current.prev
        new_node = Node(data)
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev= new_node
        self.size += 1

    def delete_at(self,index):
        if index < 0 or index > self.size:
            raise IndexError("Linked List is Empty")
        if index == 0:
            return self.delete_first()
        if index == self.size:
            return self.delete_last
        if index <= self.size // 2:
            current = self.head
            for i in range(index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.size-index -1):
                current = current.prev
        deleted_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return deleted_data

    def delete_node(self,node):
        """Delete specific node - O(1) if you have node reference!"""
        if not node:
            return
        if node == self.head:
            return self.delete_first()
        if node == self.tail:
            return self.delete_last()
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.data
    
    def find(self,target):
        """Find element and return index - O(n)"""
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
        return -1
    
    def find_node(self,target):
        """Find and return the actual node - O(n)"""
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None

    def get(self,index):
        """Get element at specific index - O(n), optimized for direction"""
        if index <0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        if index <= self.size//2:
            current = self.head
            for i in range(index):
                current =  current.next
        else:
            current = self.tail
            for i in range(self.size - index- 1):
                current = current.prev
        return current.data

    def reverse(self):
        """Reverse the linked list - O(n)"""
        current = self.head
        self.head,self.tail = self.tail,self.head
        while current:
            current.prev,current.next = current.next,current.prev
            current = current.prev

    def display_forward(self):
        """Display from head to tail"""
        if self.is_empty():
            return "Empty list"

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "None <- " +"<->".join(elements)+"-> None"


    def display_backward(self):
        """Display from tail to head (if you add tail pointer)"""
        if self.is_empty():
            return "Empty list"

        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return "None <- "+"<->".join(elements)+ "->None"
    
    def to_list_forward(self):
        """Convert to Python list (forward) - O(n)"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current =current.next
        return elements

    def to_list_backward(self):
        """Convert to Python list (backward) - O(n)"""
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current =current.prev
        return elements

    def __len__(self):
        return self.size

    def __str__(self):
        return self.display_forward()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def iter_backward(self):
        current = self.tail
        while current:
            yield current.data
            current = current.prev

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