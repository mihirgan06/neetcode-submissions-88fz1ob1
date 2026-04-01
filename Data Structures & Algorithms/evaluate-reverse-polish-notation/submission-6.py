class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #solve the equation when in reverse polish notation
        '''
        We need to read it as the operators come after the operands but 
        evaluate the expression normally


        Iterate through the array of tokens pushing into the stack
        if we hit an operand, and then we want to jsut compute it pop and pushbac
        '''
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:

                if token == '+':
                    top = stack.pop()
                    top2 = stack.pop()
                    stack.append(int(top) + int(top2))
                elif token == '-':
                    top = stack.pop()
                    top2 = stack.pop()
                    stack.append(int(top2) - int(top))  
                elif token == '*':
                    top = stack.pop()
                    top2 = stack.pop()
                    stack.append(int(top) * int(top2))
                elif token == '/':
                    top = stack.pop()
                    top2 = stack.pop()
                    stack.append(int(top2/top))
        return stack[-1]
