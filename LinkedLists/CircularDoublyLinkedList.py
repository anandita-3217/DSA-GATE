class DLLNode:
    def __init__(self,data,next = None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.data)
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def prepend(self,data):
        new_node = DLLNode(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail

            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node
        self.size += 1
    
    def delete_first(self):
        if self.is_empty():
            raise ValueError("Linked List is empty!")
        deleted_data = self.head.data
        if self.size == 1:
            self.head = None
        else:
            tail = self.head.prev
            new_head = self.head.next
            tail.next = new_head
            new_head.prev= tail
            self.head = new_head
        self.size -= 1
        return deleted_data
    
    def append(self,data):
        new_node = DLLNode(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail

            tail.next = new_node
            self.head.prev = new_node
        self.size += 1

    def delete_last(self):
        if self.is_empty():
            raise ValueError("Linked List is Empty!")
        if self.size == 1:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        tail = self.head.prev
        new_tail = tail.prev
        deleted_data = tail.data
        new_tail.next = self.head
        self.head.prev = new_tail
        self.size -= 1
        return deleted_data
    
    def insert_at(self,index,data):
        if index < 0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return 
        current = self.head
        for i in range(index):
            current = current.next
        
        new_node = DLLNode(data)
        new_node.next = current
        new_node.prv = current.prev

        current.prev.next = new_node
        current.prev = new_node

        self.size += 1

    def delete_at(self,index):
        if self.is_empty():
            raise ValueError("List is Empty")
        if index < 0 or index > self.size:
            raise("Index Out of Bounds")
        if index == 0:
            return self.delete_first()
        if index == self.size -1 :
            return self.delete_last()
        
        current = self.head
        for i in range(index):
            current =current.next
        deleted_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return deleted_data
    
    def find(self,target):
        if self.is_empty():
            raise ValueError("Linked List is Empty")
        current = self.head
        for i in range(self.size):
            if current.data == target:
                return i
            current =current.next
        return -1
    
    def get(self,index):
        if self.is_empty():
            raise ValueError("Linked List is Empty")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    
    def display_forward(self):
        if self.is_empty():
            return "Linked List is Empty"
        
        elements = []
        current = self.head
        elements.append(str(current.data))
        for i in range(self.size):
            elements.append(str(current.next))
            current =  current.next
        return "-> ".join(elements) +" <-> (circular)"
    
    def display_backward(self):
        if self.is_empty():
            return "Linked List is Empty"
        
        elements = []
        current = self.head.prev
        elements.append(str(current.data))
        for i in range(self.size):
            elements.append(str(current.next))
            current =  current.prev
        return "<-> ".join(elements) +" <-> (circular)"

    def to_list_forward(self):
        if self.is_empty():
            return []
        elements = []
        current = self.head
        for i in range (self.size):
            elements.append(current.data)
            current = current.next
        return elements

    def to_list_backward(self):
        if self.is_empty():
            return []
        elements = []
        current = self.head.prev
        for i in range (self.size):
            elements.append(current.data)
            current = current.prev
        return elements

    def __len__(self):
        return self.size
    
    def __str__(self):
        return self.display_forward()

    def __iter__(self):
        if self.is_empty():
            return
        current = self.head
        for i in range(self.size):
            yield current.data
            current = current.next
if __name__ == "__main__":

    print("\n=== Doubly Circular LinkedList Demo ===")
    
    # Create doubly circular list
    dcl = CircularDoublyLinkedList()
    
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