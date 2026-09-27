class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
            given an array of strings tokens
            - operands may be integers or the results of other operations
            tokens = ["1","2","+","3","*","4","-"]
            operators include '+', '-', '*', and '/'.


            ((1 + 2) * 3) - 4 = 9 - 4 = 5

            Iterate through the stack append the values to the stack
            when we encounter an operand we pop from the relevant values from the stack and ocmpute the result



        '''
        stack = []
        result = 0
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a/b))
        return stack[-1]