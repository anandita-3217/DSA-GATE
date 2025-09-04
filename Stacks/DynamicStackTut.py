class Node:
    """Node class for the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class LinkedListStack:
    """Stack implementation using a singly linked list"""
    
    def __init__(self):
        self.top = None  # Points to the top of the stack (head of linked list)
        self.size = 0
    
    def is_empty(self):
        """Check if the stack is empty"""
        return self.top is None
    
    def get_size(self):
        """Return the number of elements in the stack"""
        return self.size
    
    def push(self, data):
        """Push an element onto the top of the stack - O(1)"""
        new_node = Node(data)
        new_node.next = self.top  # New node points to current top
        self.top = new_node       # Update top to point to new node
        self.size += 1
        print(f"Pushed: {data}")
    
    def pop(self):
        """Remove and return the top element from the stack - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty - cannot pop")
        
        data = self.top.data      # Get data from top node
        self.top = self.top.next  # Move top to next node
        self.size -= 1
        return data
    
    def peek(self):
        """Return the top element without removing it - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty - cannot peek")
        
        return self.top.data
    
    def display(self):
        """Display the stack from top to bottom"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        current = self.top
        stack_elements = []
        
        while current:
            stack_elements.append(str(current.data))
            current = current.next
        
        # Display with visual representation
        print("    " + " <- TOP")
        for i, element in enumerate(stack_elements):
            print(f"[{element:^3}]")
        print("    " + " <- BOTTOM")
        print(f"Size: {self.size}")
    
    def clear(self):
        """Clear all elements from the stack"""
        self.top = None
        self.size = 0
        print("Stack cleared")
    
    def to_list(self):
        """Convert stack to a list (top to bottom order)"""
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def search(self, data):
        """Search for an element and return its position from top (0-indexed)"""
        current = self.top
        position = 0
        
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found

# Additional Stack Applications
class BalancedParentheses:
    """Class to check balanced parentheses using stack"""
    
    @staticmethod
    def is_balanced(expression):
        """Check if parentheses are balanced in an expression"""
        stack = LinkedListStack()
        opening = "([{"
        closing = ")]}"
        pairs = {"(": ")", "[": "]", "{": "}"}
        
        for char in expression:
            if char in opening:
                stack.push(char)
            elif char in closing:
                if stack.is_empty():
                    return False
                
                top = stack.pop()
                if pairs[top] != char:
                    return False
        
        return stack.is_empty()

class PostfixEvaluator:
    """Class to evaluate postfix expressions using stack"""
    
    @staticmethod
    def evaluate(expression):
        """Evaluate a postfix expression"""
        stack = LinkedListStack()
        operators = {'+', '-', '*', '/', '//', '%', '**'}
        
        tokens = expression.split()
        
        for token in tokens:
            if token not in operators:
                # It's a number
                stack.push(float(token))
            else:
                # It's an operator
                if stack.get_size() < 2:
                    raise ValueError("Invalid postfix expression")
                
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = operand1 / operand2
                elif token == '//':
                    result = operand1 // operand2
                elif token == '%':
                    result = operand1 % operand2
                elif token == '**':
                    result = operand1 ** operand2
                
                stack.push(result)
        
        if stack.get_size() != 1:
            raise ValueError("Invalid postfix expression")
        
        return stack.pop()

# Example usage and testing
if __name__ == "__main__":
    print("=== Linked List Stack Implementation ===\n")
    
    # Create a new stack
    stack = LinkedListStack()
    
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
    
    # Test balanced parentheses
    print("\n5. Testing Balanced Parentheses:")
    test_expressions = [
        "((()))",
        "({[]})",
        "(()",
        "([)]",
        "{[()]}",
        "((("
    ]
    
    for expr in test_expressions:
        result = BalancedParentheses.is_balanced(expr)
        print(f"'{expr}' is balanced: {result}")
    
    # Test postfix evaluation
    print("\n6. Testing Postfix Expression Evaluation:")
    postfix_expressions = [
        "3 4 + 2 *",        # (3 + 4) * 2 = 14
        "15 7 1 1 + - / 3 * 2 1 1 + + -",  # Complex expression
        "5 1 2 + 4 * + 3 -" # 5 + ((1 + 2) * 4) - 3 = 14
    ]
    
    evaluator = PostfixEvaluator()
    for expr in postfix_expressions:
        try:
            result = evaluator.evaluate(expr)
            print(f"'{expr}' = {result}")
        except Exception as e:
            print(f"Error evaluating '{expr}': {e}")
    
    # Test error conditions
    print("\n7. Testing error conditions:")
    empty_stack = LinkedListStack()
    
    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"Pop from empty stack: {e}")
    
    try:
        empty_stack.peek()
    except IndexError as e:
        print(f"Peek at empty stack: {e}")
    
    print("\n=== Stack Implementation Complete ===")