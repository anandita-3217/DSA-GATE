# Stack Data Structure - GATE 2026 Cheat Sheet

## 🥞 What is a Stack?

**Think:** A stack of plates! You can only add/remove from the TOP.

**LIFO Principle:** Last In, First Out
- Last plate you put on = First plate you take off
- Like your browser's back button or Ctrl+Z undo

---

## 🔧 Basic Operations

| Operation | Description | Time Complexity |
|-----------|-------------|----------------|
| **push(x)** | Add element to top | O(1) |
| **pop()** | Remove & return top element | O(1) |
| **peek()/top()** | View top element (don't remove) | O(1) |
| **isEmpty()** | Check if stack is empty | O(1) |
| **size()** | Get number of elements | O(1) |

**Memory Trick:** "PUSH down, POP up, PEEK over!"

---

## 💻 Python Implementation

### Method 1: Using List (Most Common)
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)  # Add to end
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()  # Remove from end
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]  # Last element
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return f"Stack: {self.items} (top → bottom)"

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)        # Stack: [1, 2, 3] (top → bottom)
print(stack.peek()) # 3
print(stack.pop())  # 3
print(stack.pop())  # 2
```

### Method 2: Using collections.deque (More Efficient)
```python
from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
```

### Method 3: Python List as Stack (Quick & Dirty)
```python
# Simple approach - just use a list directly!
stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)

# Pop
top = stack.pop()  # Returns 3
peek = stack[-1]   # Look at top without removing

# Check empty
is_empty = len(stack) == 0
```

---

## 🎯 Classic Stack Applications

### 1. Parentheses/Bracket Matching ✅
```python
def is_balanced(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack:
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

# Test
print(is_balanced("((()))"))     # True
print(is_balanced("([{}])"))     # True  
print(is_balanced("([)]"))       # False
```

### 2. Infix to Postfix Conversion 🔄
```python
def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    postfix = []
    
    for char in infix:
        if char.isalnum():  # Operand
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[char]):
                postfix.append(stack.pop())
            stack.append(char)
    
    # Pop remaining operators
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

# Test
print(infix_to_postfix("A+B*C"))      # ABC*+
print(infix_to_postfix("(A+B)*C"))    # AB+C*
```

### 3. Evaluate Postfix Expression 🧮
```python
def evaluate_postfix(postfix):
    stack = []
    
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:  # Operator
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)  # Integer division
    
    return stack[0]

# Test
print(evaluate_postfix("23*5+"))  # 2*3+5 = 11
```

### 4. Next Greater Element 📈
```python
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    
    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        # Pop elements smaller than current
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # If stack not empty, top is next greater
        if stack:
            result[i] = stack[-1]
        
        # Push current element
        stack.append(arr[i])
    
    return result

# Test
print(next_greater_element([4, 5, 2, 25]))  # [5, 25, 25, -1]
```

### 5. Function Call Stack (Recursion Simulation) 🔄
```python
def factorial_iterative(n):
    stack = []
    
    # Push all numbers from n to 1
    for i in range(n, 0, -1):
        stack.append(i)
    
    result = 1
    while stack:
        result *= stack.pop()
    
    return result

print(factorial_iterative(5))  # 120
```

---

## 🧠 GATE Exam Essentials

### Stack vs Other Data Structures
| Feature | Stack | Queue | Array |
|---------|-------|-------|-------|
| **Access** | Top only | Front/Rear | Any index |
| **Insertion** | Top (push) | Rear (enqueue) | Any index |
| **Deletion** | Top (pop) | Front (dequeue) | Any index |
| **Order** | LIFO | FIFO | Random |

### Common GATE Question Types

#### 1. Stack Operations Trace
```
Given: push(1), push(2), pop(), push(3), pop(), pop()
Stack states: [] → [1] → [1,2] → [1] → [1,3] → [1] → []
Output sequence: 2, 3, 1
```

#### 2. Stack Overflow/Underflow
- **Overflow**: Trying to push when stack is full
- **Underflow**: Trying to pop from empty stack

#### 3. Expression Conversion Priorities
```
Infix: A + B * C - D
Postfix: A B C * + D -
Prefix: - + A * B C D
```

#### 4. Recursion → Stack Conversion
Every recursive call = one stack frame

### Memory Tricks for GATE! 🎯

#### **Stack Applications Mnemonic: "PRIN-E"**
- **P**arentheses matching
- **R**ecursion (function calls)  
- **I**nfix/Postfix conversion
- **N**ext greater element
- **E**xpression evaluation

#### **Stack vs Queue: "LIFO vs FIFO"**
- Stack = **LIFO** = "**L**ast **I**n **F**irst **O**ut" = Plates
- Queue = **FIFO** = "**F**irst **I**n **F**irst **O**ut" = Line at movies

#### **Postfix Evaluation Rule:**
"**Operands go on stack, operators pop two and push result**"

### Implementation Details for GATE
```python
# Fixed-size stack (array implementation)
class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1  # Index of top element
    
    def push(self, item):
        if self.top == self.capacity - 1:
            raise Exception("Stack Overflow")
        self.top += 1
        self.items[self.top] = item
    
    def pop(self):
        if self.top == -1:
            raise Exception("Stack Underflow")
        item = self.items[self.top]
        self.top -= 1
        return item
```

### Quick Complexity Summary
- **Time Complexity**: All operations O(1)
- **Space Complexity**: O(n) where n = number of elements
- **Best for**: When you need LIFO behavior
- **Avoid for**: Random access or FIFO operations