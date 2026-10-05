class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
            Given:
                array of strings tokens that represent a valid arithmetic expression in RPN
            tokens = ["1","2","+","3","*","4","-"]

            append 1 and 2 to a stack
            then pop 1 and 2 and compute then add back to the stack
            the operations will always between 2 numbers


        '''

        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val1 - val2)
                elif token == "*":
                    stack.append(val1 * val2)
                elif token == "/":
                    stack.append(int(val1 / val2))
        return stack[-1]
        