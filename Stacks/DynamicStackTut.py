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
    # 🥞 StackApplications Class - All the Stack Magic in One Place!
# Perfect for GATE DA 2026 preparation

class StackApplications:
    """
    A comprehensive class demonstrating 5 crucial stack applications.
    Each method is self-contained and includes step-by-step explanations!
    """
    
    def __init__(self):
        """
        Initialize the StackApplications class.
        We'll use Python lists as stacks (append = push, pop = pop)
        """
        self.debug = True  # Set to True to see step-by-step process
    
    def set_debug(self, debug_mode):
        """Enable/disable step-by-step debugging output"""
        self.debug = debug_mode
    
    # ============================================================
    # 1️⃣ PARENTHESES/BRACKET MATCHING
    # ============================================================
    
    def is_balanced_parentheses(self, expression):
        """
        Check if parentheses/brackets are balanced in an expression.
        
        Examples:
        - "((()))" → True
        - "([{}])" → True  
        - "((())" → False
        - "([)]" → False
        
        Logic: Use stack to track opening brackets, pop when closing found.
        """
        if self.debug:
            print(f"\n🔍 Checking if '{expression}' has balanced brackets...")
        
        stack = []
        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        opening_brackets = set(['(', '{', '['])
        
        for i, char in enumerate(expression):
            if self.debug:
                print(f"  Step {i+1}: Processing '{char}', Stack: {stack}")
            
            if char in opening_brackets:
                # Opening bracket - push to stack
                stack.append(char)
                if self.debug:
                    print(f"    → Opening bracket, pushed to stack")
            
            elif char in bracket_map:
                # Closing bracket
                if not stack:
                    if self.debug:
                        print(f"    → Closing bracket but stack empty! ❌")
                    return False
                
                top = stack.pop()
                expected = bracket_map[char]
                
                if top != expected:
                    if self.debug:
                        print(f"    → Mismatch! Expected '{expected}' but got '{top}' ❌")
                    return False
                
                if self.debug:
                    print(f"    → Matched '{top}' with '{char}' ✅")
        
        # Stack should be empty for balanced expression
        is_balanced = len(stack) == 0
        
        if self.debug:
            if is_balanced:
                print(f"  Result: Balanced! ✅")
            else:
                print(f"  Result: Unbalanced! Remaining: {stack} ❌")
        
        return is_balanced
    
    # ============================================================
    # 2️⃣ INFIX TO POSTFIX CONVERSION
    # ============================================================
    
    def infix_to_postfix(self, infix_expression):
        """
        Convert infix expression to postfix using Shunting Yard algorithm.
        
        Examples:
        - "A+B" → "AB+"
        - "A+B*C" → "ABC*+"
        - "(A+B)*C" → "AB+C*"
        
        Logic: Use stack for operators, handle precedence and associativity.
        """
        if self.debug:
            print(f"\n🔄 Converting '{infix_expression}' from infix to postfix...")
        
        # Define operator precedence (higher number = higher precedence)
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        
        # Right associative operators
        right_associative = {'^'}
        
        stack = []  # Operator stack
        postfix = []  # Output list
        
        for i, token in enumerate(infix_expression):
            if self.debug:
                print(f"  Step {i+1}: Processing '{token}'")
                print(f"    Stack: {stack}, Output: {''.join(postfix)}")
            
            if token.isalnum():  # Operand (letter or number)
                postfix.append(token)
                if self.debug:
                    print(f"    → Operand: Added '{token}' to output")
            
            elif token == '(':  # Left parenthesis
                stack.append(token)
                if self.debug:
                    print(f"    → Left parenthesis: Pushed to stack")
            
            elif token == ')':  # Right parenthesis
                # Pop operators until left parenthesis
                while stack and stack[-1] != '(':
                    op = stack.pop()
                    postfix.append(op)
                    if self.debug:
                        print(f"    → Popped '{op}' to output")
                
                if stack:  # Remove the left parenthesis
                    stack.pop()
                    if self.debug:
                        print(f"    → Removed matching '(' from stack")
            
            elif token in precedence:  # Operator
                # Pop operators with higher or equal precedence
                while (stack and 
                       stack[-1] != '(' and 
                       stack[-1] in precedence and
                       (precedence[stack[-1]] > precedence[token] or
                        (precedence[stack[-1]] == precedence[token] and 
                         token not in right_associative))):
                    
                    op = stack.pop()
                    postfix.append(op)
                    if self.debug:
                        print(f"    → Popped higher precedence '{op}' to output")
                
                stack.append(token)
                if self.debug:
                    print(f"    → Pushed operator '{token}' to stack")
        
        # Pop remaining operators
        while stack:
            op = stack.pop()
            postfix.append(op)
            if self.debug:
                print(f"  Final: Popped '{op}' to output")
        
        result = ''.join(postfix)
        if self.debug:
            print(f"  Result: '{infix_expression}' → '{result}' ✅")
        
        return result
    
    # ============================================================
    # 3️⃣ POSTFIX EXPRESSION EVALUATION
    # ============================================================
    
    def evaluate_postfix(self, postfix_expression, variables=None):
        """
        Evaluate a postfix expression and return the result.
        
        Examples:
        - "23+" → 5
        - "23*4+" → 10
        - "AB+C*" with A=2, B=3, C=4 → 20
        
        Logic: Use stack to store operands, pop two when operator found.
        """
        if variables is None:
            variables = {}
        
        if self.debug:
            print(f"\n🧮 Evaluating postfix expression '{postfix_expression}'")
            if variables:
                print(f"  Variables: {variables}")
        
        stack = []
        
        for i, token in enumerate(postfix_expression):
            if self.debug:
                print(f"  Step {i+1}: Processing '{token}', Stack: {stack}")
            
            if token.isdigit():  # Single digit number
                stack.append(int(token))
                if self.debug:
                    print(f"    → Number: Pushed {token} to stack")
            
            elif token.isalpha() and token in variables:  # Variable
                value = variables[token]
                stack.append(value)
                if self.debug:
                    print(f"    → Variable: {token} = {value}, pushed to stack")
            
            elif token in ['+', '-', '*', '/', '^']:  # Operator
                if len(stack) < 2:
                    raise ValueError(f"Invalid expression: Not enough operands for '{token}'")
                
                # Pop two operands (order matters!)
                operand2 = stack.pop()  # Second operand
                operand1 = stack.pop()  # First operand
                
                # Perform operation
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = operand1 / operand2
                elif token == '^':
                    result = operand1 ** operand2
                
                stack.append(result)
                
                if self.debug:
                    print(f"    → Operation: {operand1} {token} {operand2} = {result}")
        
        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")
        
        final_result = stack[0]
        if self.debug:
            print(f"  Final Result: {final_result} ✅")
        
        return final_result
    
    # ============================================================
    # 4️⃣ NEXT GREATER ELEMENT
    # ============================================================
    
    def next_greater_element(self, arr):
        """
        Find the next greater element for each element in the array.
        
        Examples:
        - [4, 5, 2, 25] → [5, 25, 25, -1]
        - [13, 7, 6, 12] → [-1, 12, 12, -1]
        
        Logic: Use stack to keep track of elements waiting for their next greater element.
        """
        if self.debug:
            print(f"\n📈 Finding next greater elements for {arr}")
        
        stack = []  # Stack stores indices, not values
        result = [-1] * len(arr)  # Initialize result with -1
        
        for i in range(len(arr)):
            if self.debug:
                print(f"  Step {i+1}: Processing arr[{i}] = {arr[i]}")
                print(f"    Stack indices: {stack}")
            
            # While stack is not empty and current element is greater
            # than the element at the index stored at top of stack
            while stack and arr[i] > arr[stack[-1]]:
                index = stack.pop()
                result[index] = arr[i]
                
                if self.debug:
                    print(f"    → Found next greater for arr[{index}]={arr[index]}: {arr[i]}")
            
            # Push current index to stack
            stack.append(i)
            
            if self.debug:
                print(f"    → Pushed index {i} to stack")
                print(f"    → Current result: {result}")
        
        if self.debug:
            print(f"  Final Result: {result} ✅")
            # Pretty print the mapping
            print("  Element → Next Greater:")
            for i, val in enumerate(arr):
                next_greater = result[i] if result[i] != -1 else "None"
                print(f"    {val} → {next_greater}")
        
        return result
    
    # ============================================================
    # 5️⃣ FUNCTION CALL STACK (RECURSION SIMULATION)
    # ============================================================
    
    def simulate_recursion(self, n, function_type="factorial"):
        """
        Simulate how the call stack works during recursion.
        
        Supported functions:
        - "factorial": Calculate n! (factorial)
        - "fibonacci": Calculate fibonacci(n)
        
        This shows how the call stack grows and shrinks during recursion.
        """
        if self.debug:
            print(f"\n🔄 Simulating {function_type}({n}) recursion...")
        
        call_stack = []  # Simulate the function call stack
        results = {}     # Store computed results
        
        if function_type == "factorial":
            return self._simulate_factorial(n, call_stack, results)
        elif function_type == "fibonacci":
            return self._simulate_fibonacci(n, call_stack, results)
        else:
            raise ValueError(f"Unsupported function type: {function_type}")
    
    def _simulate_factorial(self, n, call_stack, results):
        """Helper method to simulate factorial recursion"""
        
        def factorial_step(n, depth=0):
            indent = "  " * depth
            
            if self.debug:
                print(f"{indent}📞 Calling factorial({n})")
            
            # Push to call stack
            call_frame = f"factorial({n})"
            call_stack.append(call_frame)
            
            if self.debug:
                print(f"{indent}   Call stack: {call_stack}")
            
            # Base case
            if n <= 1:
                result = 1
                if self.debug:
                    print(f"{indent}   Base case: factorial({n}) = {result}")
            else:
                # Recursive case
                if self.debug:
                    print(f"{indent}   Recursive case: factorial({n}) = {n} * factorial({n-1})")
                
                # Make recursive call
                recursive_result = factorial_step(n-1, depth+1)
                result = n * recursive_result
                
                if self.debug:
                    print(f"{indent}   Returning: {n} * {recursive_result} = {result}")
            
            # Pop from call stack
            call_stack.pop()
            
            if self.debug:
                print(f"{indent}🔙 Returning from factorial({n}) = {result}")
                print(f"{indent}   Call stack after return: {call_stack}")
            
            return result
        
        return factorial_step(n)
    
    def _simulate_fibonacci(self, n, call_stack, results):
        """Helper method to simulate fibonacci recursion"""
        
        def fibonacci_step(n, depth=0):
            indent = "  " * depth
            
            if self.debug:
                print(f"{indent}📞 Calling fibonacci({n})")
            
            # Push to call stack
            call_frame = f"fibonacci({n})"
            call_stack.append(call_frame)
            
            if self.debug:
                print(f"{indent}   Call stack: {call_stack}")
            
            # Base cases
            if n <= 1:
                result = n
                if self.debug:
                    print(f"{indent}   Base case: fibonacci({n}) = {result}")
            else:
                # Recursive case
                if self.debug:
                    print(f"{indent}   Recursive: fibonacci({n}) = fibonacci({n-1}) + fibonacci({n-2})")
                
                # Make recursive calls
                fib1 = fibonacci_step(n-1, depth+1)
                fib2 = fibonacci_step(n-2, depth+1)
                result = fib1 + fib2
                
                if self.debug:
                    print(f"{indent}   Returning: {fib1} + {fib2} = {result}")
            
            # Pop from call stack
            call_stack.pop()
            
            if self.debug:
                print(f"{indent}🔙 Returning from fibonacci({n}) = {result}")
            
            return result
        
        return fibonacci_step(n)
    
    # ============================================================
    # 🎮 DEMO METHODS - Test All Applications!
    # ============================================================
    
    def demo_all_applications(self):
        """Run demonstrations of all 5 stack applications"""
        
        print("🥞 STACK APPLICATIONS DEMO")
        print("=" * 50)
        
        # 1. Parentheses Matching
        print("\n1️⃣ PARENTHESES/BRACKET MATCHING")
        print("-" * 35)
        test_expressions = [
            "((()))",      # Balanced
            "([{}])",      # Balanced with different brackets
            "((())",       # Unbalanced
            "([)]",        # Wrong order
            "{[()]}",      # Nested and balanced
        ]
        
        for expr in test_expressions:
            result = self.is_balanced_parentheses(expr)
            status = "✅ Balanced" if result else "❌ Unbalanced"
            print(f"'{expr}' → {status}")
        
        # 2. Infix to Postfix
        print("\n2️⃣ INFIX TO POSTFIX CONVERSION")
        print("-" * 35)
        infix_expressions = [
            "A+B",
            "A+B*C", 
            "(A+B)*C",
            "A+B*C-D",
            "A^B^C",  # Right associative
        ]
        
        for expr in infix_expressions:
            postfix = self.infix_to_postfix(expr)
            print(f"'{expr}' → '{postfix}'")
        
        # 3. Postfix Evaluation
        print("\n3️⃣ POSTFIX EVALUATION")
        print("-" * 25)
        postfix_expressions = [
            ("23+", None),
            ("234*+", None),
            ("ABC*+", {"A": 2, "B": 3, "C": 4}),
        ]
        
        for expr, vars in postfix_expressions:
            try:
                result = self.evaluate_postfix(expr, vars)
                print(f"'{expr}' = {result}")
            except Exception as e:
                print(f"'{expr}' → Error: {e}")
        
        # 4. Next Greater Element
        print("\n4️⃣ NEXT GREATER ELEMENT")
        print("-" * 25)
        arrays = [
            [4, 5, 2, 25],
            [13, 7, 6, 12],
            [1, 2, 3, 4, 5],
        ]
        
        for arr in arrays:
            result = self.next_greater_element(arr)
            print(f"{arr} → {result}")
        
        # 5. Recursion Simulation
        print("\n5️⃣ FUNCTION CALL STACK SIMULATION")
        print("-" * 35)
        
        # Factorial
        print("Factorial(4):")
        result = self.simulate_recursion(4, "factorial")
        print(f"Result: {result}")
        
        print("\nFibonacci(4):")
        result = self.simulate_recursion(4, "fibonacci")
        print(f"Result: {result}")

# ============================================================
# 🚀 USAGE EXAMPLES
# ============================================================

if __name__ == "__main__":
    # Create the stack applications instance
    stack_apps = StackApplications()
    
    # Run the full demo
    stack_apps.demo_all_applications()
    
    # You can also test individual methods:
    print("\n" + "="*50)
    print("🧪 INDIVIDUAL TESTING")
    print("="*50)
    
    # Test specific functionality
    print("\nTesting bracket matching:")
    print(stack_apps.is_balanced_parentheses("({[]})"))  # Should be True
    
    print("\nTesting infix to postfix:")
    postfix = stack_apps.infix_to_postfix("(A+B)*C")
    print(f"Postfix: {postfix}")
    
    print("\nTesting postfix evaluation:")
    result = stack_apps.evaluate_postfix("23+4*", None)
    print(f"Result: {result}")
    
    # Turn off debug mode for cleaner output
    print("\n--- With debug mode OFF ---")
    stack_apps.set_debug(False)
    
    result = stack_apps.next_greater_element([4, 5, 2, 25, 3])
    print(f"Next greater elements: {result}")