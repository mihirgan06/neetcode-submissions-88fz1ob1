class Solution:
    def isValid(self, s: str) -> bool:
        #Goal O(N) time complexity
        #O(N) space, create a stack to hold everything
        #if the length of string is odd, we know the number of paretheses is incorrect

        if len(s) % 2 != 0:
            return False

        stack = []

        for ch in s:
            #push each character in the string into the stack
            if ch in "([{":
                stack.append(ch)
            
            elif ch in ")]}":
                if not stack:
                    return False
                if ch == "}" and stack[-1] != "{":
                    return False
                if ch == ")" and stack[-1] != "(":
                    return False
                if ch == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        
        return True
        
        
        
