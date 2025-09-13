class StackApplications:
    """
    A comprehensive class demonstrating 5 crucial stack applications.
    Each method is self-contained and includes step-by-step explanations!
    """
    def __init__(self):
        self.debug = False
    def set_debug(self,debug_mode):
        self.debug = debug_mode
    # def is_balanced_parentheses(self,expression):
    #     """
    #     Check if parentheses/brackets are balanced in an expression.
        
    #     Examples:
    #     - "((()))" → True
    #     - "([{}])" → True  
    #     - "((())" → False
    #     - "([)]" → False
        
    #     Logic: Use stack to track opening brackets, pop when closing found.
    #     """
    #     if self.debug:
    #         print(f"\n Checking if {expression} has balanced parentheses")
    #     stack = []
    #     bracket_map ={')': '(' ,'}': '{' ,']':' ['}
    #     opening_brackets = set(['(','[','{'])
    #     for i, char in enumerate(expression):
    #         if self.debug:
    #             print(f"  Step {i+1}: Processing '{char}', Stack: {stack}")
    #         if char in opening_brackets:
    #             stack.append(char)
    #         if self.debug:
    #             if self.debug:
    #                 print(f"    → Opening bracket, pushed to stack")
    #         elif char in bracket_map:
    #             if not stack:
    #                 if self.debug:
    #                     print(f"    → Closing bracket but stack empty! ❌")
    #                 return False
    #             top = stack.pop()
    #             expected = bracket_map[char]
    #             if top != expected:
    #                 if self.debug:
    #                     print(f"    → Mismatch! Expected '{expected}' but got '{top}' ❌")
    #                 return False
    #             if self.debug:
    #                 print(f"    → Matched '{top}' with '{char}' ✅")
    #     is_balanced = len(stack) == 0
    #     if self.debug:
    #         if is_balanced:
    #             print(f"  Result: Balanced! ✅")
    #         else:
    #             print(f"  Result: Unbalanced! Remaining: {stack} ❌")
    #     return is_balanced
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
    

    def infix_to_postfix(self,infix_expression):
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
        precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
        right_associative = {'^'}
        stack = []
        postfix =[]
        for i,token in enumerate(infix_expression):
            if self.debug:
                print(f"  Step {i+1}: Processing '{token}'")
                print(f"    Stack: {stack}, Output: {''.join(postfix)}")
            if token.isalnum():
                postfix.append(token)
                if self.debug:
                    print(f"    → Operand: Added '{token}' to output")
            elif token == '(':
                stack.append(token)
                if self.debug:
                    print(f"    → Left parenthesis: Pushed to stack")
            elif token == ')':
                while stack and stack[-1] !='(':
                    op = stack.pop()
                    postfix.append(op)
                    if self.debug:
                        print(f"    → Popped '{op}' to output")
                if stack:
                    stack.pop()
                    if self.debug:
                        print(f"    → Removed matching '(' from stack")
            elif token and precedence:
                while (stack and stack[-1] != '(' and stack[-1] in precedence and 
                    (precedence[stack[-1]] > precedence[token] or 
                        (precedence[stack[-1]] == precedence[token] and token not in right_associative))):
                    op = stack.pop()
                    postfix.append(op)
                    if self.debug:
                        print(f"    → Popped higher precedence '{op}' to output")
                stack.append(token)
                if self.debug:
                    print(f"    → Pushed operator '{token}' to stack")
        while stack:
            op = stack.pop()
            postfix.append(op)
            if self.debug:
                print(f"  Final: Popped '{op}' to output")
        result = ''.join(postfix)
        if self.debug:
            print(f"    Result: '{infix_expression}' -> '{result}")
        return result

if __name__ == "__main__":
    stack_apps = StackApplications()
    print("\nTesting bracket matching:")
    print(stack_apps.is_balanced_parentheses("({[]})"))  # Should be True
    
    print("\nTesting infix to postfix:")
    postfix = stack_apps.infix_to_postfix("(A+B)*C")
    print(f"Postfix: {postfix}")