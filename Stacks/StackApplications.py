class StackApplications:
    """
    A comprehensive class demonstrating 5 crucial stack applications.
    Each method is self-contained and includes step-by-step explanations!
    """
    def __init__(self):
        self.debug = False
    def set_debug(self,debug_mode):
        self.debug = debug_mode
    def is_balanced_parentheses(self,expression):
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
            print(f"\n Checking if the '{expression}' has balanced parenthses")
        stack = []
        bracket_map = {')':'(','}':'{',']':'['}
        opening_brackets = set(['(','[','{'])
        for i,char in enumerate(expression):
            if self.debug:
                print(f"    Step {i+1}: Processing '{char}', Stack: '{stack}'")
            if char in opening_brackets:
                stack.append(char)
                if self.debug:
                    print(f"    ->Opening bracket, pushed to stack")
            elif char in bracket_map:
                if not stack:
                    if self.debug:
                        print(f"    -> Closing bracket but stack is empty so obviously unbalanced")
                    return False
                top = stack.pop()
                expected = bracket_map[char]
                if top != expected:
                    if self.debug:
                        print(f"    -> Mismatch! Expected '{expected}' but got '{top}' ")
                    return False
                if self.debug:
                    print(f"    → Matched '{top}' with '{char}' ✅")
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

    def postfix_evaluation(self,postfix_expression,variables=None):
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
            print(f"Evaluating postfix expression '{postfix_expression}'")
            if variables:
                print(f"    Variables: {variables}")

        stack =[]
        for i,token in enumerate(postfix_expression):
            if self.debug:
                print(f"    Step {i+1}: Processing '{token}',Stack: {stack} ")
            if token.isdigit():
                stack.append(int(token))
                if self.debug:
                    print(f"    -> Number: Pushed {token} to stack")
            elif token.isalpha() and token in variables:
                value = variables[token]
                stack.append(value)
                if self.debug:
                    print(f"    -> Variable: {token} = {value},pushed to stack ")
            elif token in ['+','-','*','/','^']:
                if len(stack) < 2:
                    raise ValueError(f"Invalid expression: Not enough operands for '{token}'")
                operand1 = stack.pop()
                operand2 = stack.pop()

                if token == '+':
                    result = operand1+operand2
                elif token == '-':
                    result = operand1-operand2
                elif token == '*':
                    result = operand1*operand2
                elif token == '/':
                    result = operand1/operand2
                elif token == '^':
                    result = operand1**operand2
                stack.append(result)
                if self.debug:
                    print(f"    -> Operation: {operand1} {token} {operand2} = {result}")
        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")
        final_result = stack[0]
        if self.debug:
            print(f"    Final Result: {final_result}")

        return final_result



if __name__ == "__main__":
    stack_apps = StackApplications()
    print("\nTesting bracket matching:")
    print(stack_apps.is_balanced_parentheses("({[]})"))  # Should be True
    
    print("\nTesting infix to postfix:")
    postfix = stack_apps.infix_to_postfix("(A+B)*C")
    print(f"Postfix: {postfix}")

    print("\n Testing Postfix Evaluation:")
    post_eval = stack_apps.postfix_evaluation("23+4*",None)
    print(f"Result of Postfix Evaluation: {post_eval}")