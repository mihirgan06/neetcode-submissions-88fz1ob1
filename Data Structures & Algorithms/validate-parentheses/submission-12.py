class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Given:
            - s containing the following characters: '(', ')', '{', '}', '[' and ']'.
            input string s is valid iff:
            1. every open bracket is closed by the same type of close bracker
            2. open brackets are closed in the correct order
            3. every close bracket has a corresponding open bracket of the same type


            hold a stack
            Push all the open brackets into the stack (LIFO)
            s = []
            push in [
            if the top of nums is ] then valid


        '''
        #odd number of parentheses
        if len(s) % 2 == 1:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top == "(" and s[i] != ")":
                    return False
                elif top == "[" and s[i] != "]":
                    return False
                elif top == "{" and s[i] != "}":
                    return False
        return len(stack) == 0