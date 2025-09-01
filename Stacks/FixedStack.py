# Stacck implemetation using arrays i.e fixed size stack
class Stack:
    def __init__(self,size):
        self.items = []
        self.size = size
    def push(self,item):
        if self.is_full():
            print("[Stack Overflow]: Stack Full! Can not add anymore!")
            return False
        self.items.append(item)
        print(f"Added {item} to stack")
    def pop(self):
        if self.is_empty():
            print('[Stack Underflow]: Stack Empty! Can not pop out of an empty list')
            return None
        remove_item = self.items.pop()
        print(f"Removed {remove_item} from stack")
        return remove_item
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def is_full(self):
        return len(self.items) == self.size

s = Stack(3)
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  
s.pop()          
s.pop()          
s.pop()  