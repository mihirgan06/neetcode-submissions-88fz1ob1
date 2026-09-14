class Solution:
    def isValid(self, s: str) -> bool:
        '''
            given a string s consisting fo following characters 
            (, ), {,} [,]
            input string is valid iff
            every open bracket is closed by same type of close bracket
            order is maintained
            every close bracket has a corresponding open bracket
        '''
        stack = []
        if len(s) % 2 != 0:
            return False
        
        
        close = ")]}"

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif ch in close:
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

            
            

