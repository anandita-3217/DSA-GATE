class SLLNode:
    def __init__(self,data,next= None):
        self.data = data 
        self.next = next
    def __str__(self):
        return str(self.data)
class Node:
    def __init__(self,data,next= None,prev=None):
        self.data = data 
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.data)
    
class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def prepend(self,data):
        new_node = SLLNode(data)
        if self.is_empty():
            new_node.next = new_node
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            new_node.next = self.head
            last.next = new_node
            self.head=new_node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise ValueError("Linked List is empty")
        deleted_data = self.head.data
        
        if self.size == 1:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        self.size -= 1
        return deleted_data

    def append(self,data):
        new_node = SLLNode(data)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            last = self.head
            while last.next != self.head:
                last =last.next
            new_node.next = self.head
            last.next = new_node
            self.head = new_node
        self.size += 1
    
    def delete_last(self):
        if self.is_empty():
            raise ValueError("Linked List is Empty")
        if self.size == 1:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
        
        current = self.head
        while current.next.next != self.head:
            current = current.next
        deleted_data = current.next.data
        current.next = self.head
        self.size -= 1
        return deleted_data

    def insert_at(self,data,index):
        if index < 0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return 
        new_node = SLLNode(data)
        current = self.head
        for i in range(index-1):
            current = current.next 
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_at(self,index):
        if index < 0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        if index == 0:
            return self.delete_first()
        current = self.head
        for i in range(index - 1):
            current = current.next
        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data

    def find(self,target):
        if self.is_empty():
            raise ValueError("Linked List is Empty")
        current = self.head
        index = 0
        if current.data == target:
            return index
        current =current.next
        index += 1
        while current != self.head:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def get(self,index):
        if index <0 or index > self.size:
            raise IndexError("index Out of Bounds")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    
    def display(self):
        if self.is_empty():
            return ("Empty Circular Linked List")
        elements = []
        current = self.head
        elements.append(str(current.data))
        current = current.next
        while current != self.head:
            elements.append(str(current.data))
            current =current.next
        return "-> ".join(elements) +"->(back to "+str(self.head.data)+" HEAD )"

    def __len__(self):
        return self.size
    def __str__(self):
        return self.display()