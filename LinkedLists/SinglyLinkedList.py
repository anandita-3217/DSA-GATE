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
    def __init__(self,data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
