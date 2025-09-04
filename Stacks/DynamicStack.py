# Stacck implemetation using Linked Lists i.e Dynamic size stack

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
    def __str__(self):
        return str(self.data)
    
class DStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size
    

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Pushed {data} to top of the stack")
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is Empty!")
        deleted_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Popped {deleted_data} from top of the stack")
        return deleted_data

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        return self.top.data
    
    def display(self):
        if self.is_empty():
            raise ValueError("Stack is Empty")
        print("Stack top to bottom")
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("    " + " <- TOP")
        for i, element in enumerate(elements):
            print(f"[{element:^3}]")
        print("    " + " <- BOTTOM")
        print(f"Size: {self.size}")
    def search(self,target):
        current = self.top
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return  -1
    
    def to_list(self):
        elements = []
        current = self.top
        elements.append(current.data)
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def clear(self):
        self.top = None
        self.size = 0
    
    def __len__(self):
        return self.size
    def __str__(self):
        return
    
if __name__ == "__main__":
    print("=== Linked List Stack Implementation ===\n")
    
    # Create a new stack
    stack = DStack()
    
    # Test basic operations
    print("1. Testing basic stack operations:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.display()
    
    print(f"\nPeek (top element): {stack.peek()}")
    print(f"Stack size: {stack.get_size()}")
    
    # Test popping elements
    print("\n2. Popping elements:")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped: {popped}")
        if not stack.is_empty():
            print(f"New top: {stack.peek()}")
    
    print(f"Stack is empty: {stack.is_empty()}")
    
    # Test with different data types
    print("\n3. Testing with different data types:")
    stack.push("Hello")
    stack.push(3.14)
    stack.push([1, 2, 3])
    stack.push({"key": "value"})
    stack.display()
    
    # Test search functionality
    print("\n4. Testing search:")
    stack.clear()
    for i in range(5):
        stack.push(i * 10)
    
    stack.display()
    print(f"Position of 20 from top: {stack.search(20)}")
    print(f"Position of 100 (not exists): {stack.search(100)}")
    
    # Test stack conversion to list
    print(f"\nStack as list: {stack.to_list()}")