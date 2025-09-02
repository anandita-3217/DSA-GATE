"""
It mainly allows efficient insertion and deletion operations compared to arrays. 
Like arrays, it is also used to implement other data structures like stack, queue and deque. 

Linked List:

Data Structure: Non-contiguous
Memory Allocation: Typically allocated one by one to individual elements
Insertion/Deletion: Efficient
Access: Sequential
Array:

Data Structure: Contiguous
Memory Allocation: Typically allocated to the whole array
Insertion/Deletion: Inefficient
Access: Random


Types
Singly Linked List
Doubly Linked List
Circular Linked List


"""
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    """ SinglyLinkedList implementation"""
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        # check if the list is empty
        return self.head is None
    
    def get_size(self):
        # Get size of the list
        return self.size
    
    def prepend(self,data):
        # add node to the begining of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):
        # Deletes data at the begining
        if self.is_empty():
            raise ValueError("List is empty")
        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data


    def append(self,data):
        # Add node to the end of the linked list
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def delete_end(self):
        # Deletes data at the end
        if self.is_empty():
            raise ValueError("List is Empty")
        if self.head.next is None:
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
    
    def insert_at(self,index,data):
        # Inserts data at given index
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index -1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at(self,index):
        # Deletes data at given index
        if index < 0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        if index == 0:
            return self.delete_first()
        current = self.head
        for i in range(index-1):
            current = current.next
        delete_data = current.data
        current.next = current.next.next
        self.size -= 1
        return delete_data
    
    def find(self,target):
        # Finds data and returns index - O(n)
        current = self.head
        index  = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self,index):
        # Get element at specific index - O(n)
        if index <0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self.head = prev
    
    def display(self):
        # Displays All elements O(n)
        if self.is_empty():
            raise ValueError("List is Empty")
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "->".join(elements)+"-> None"
    
    def to_list(self):
        # Converts all elements to a list O(n)
        if self.is_empty():
            raise ValueError("List Empty!")
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    def __len__(self):
        # support for len()
        return self.size
    
    def __str__(self):
        return self.display()
    
    def __iter__(self):
        # Make the list iterable
        current = self.head
        while current:
            yield current.data
            current = current.next

if __name__ == "__main__":
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