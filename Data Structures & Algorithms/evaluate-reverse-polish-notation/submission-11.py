class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
            Given array of strings tokens
            we can get smt like 
            1, 2, +, 3, *
            and need to do 
            (1+2)*3

            makes sense makes sense
            so we just need an O(N) solution to this
            create a stack
            iterate through the tokens
            first push the first number

            we want to pop the correct value, so do we just cimpute it like and return stacj, idts

            

        '''
        stack = []
        val = 0
        for i, token in enumerate(tokens):
            if token not in "+-*/":
                stack.append(token)
            val_sum = 0
            val_sub = 0
            val_mult = 0
            val_div = 0
            if token == "+" and stack:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val1) + int(val2))
            elif token == "-" and stack:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2) - int(val1))
            elif token == "*" and stack:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2) * int(val1))
            elif token == "/" and stack:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(int(val2) / int(val1)))
            
            val = stack[-1]
        return val


        