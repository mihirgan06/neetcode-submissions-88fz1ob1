class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #given array of tokens with the RPN totation
        #we return an integer that represents the result of operations
        stack = []
        for token in tokens:
            #if the token is an integer we just want to insert it into the stack
            if token not in "+-*/":
                stack.append(token)
            #if the token is an operator, we want to empty the stack and compute
            else:
                if token == "+":
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = int(operand1) + int(operand2)
                    stack.append(result)
                elif token == "-":
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = int(operand1) - int(operand2)
                    stack.append(result)
                elif token == "*":
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = int(operand1) * int(operand2)
                    stack.append(result)
                elif token == "/":
                    operand2 = int(stack.pop())
                    operand1 = int(stack.pop())
                    result = ((operand1) / (operand2)) 
                    stack.append(result)
        return int(stack.pop())

                
                
                        

        