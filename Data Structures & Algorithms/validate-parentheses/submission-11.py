class Solution:
    def isValid(self, s: str) -> bool:
        '''
            given a string s consisting of the folliwn characters
            '(', ')', '{', '}', '[' and ']'.
            input string is valid iff:
            - each open bracket is closed by the same type of close bracket
            - open brackets are closed in the correct order
            - every close bracket has a corresponding open bracket of the same type
            s = '[]'
            true

            Observations:
            - even number of parentheses
            s = "([{}])"
            stack
            iterate through parentheses
            add the first open
            add the close 
            addthe curly
            now no more open
            now pop from stack if it matches the top of the array where were at were good 


        '''
        #odd number of parentheses --> false
        if len(s) % 2 == 1:
            return False

        stack = []

        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                next_open = stack.pop()
                if next_open == "{" and s[i] != "}":
                    return False
                elif next_open == "[" and s[i] != "]":
                    return False
                elif next_open == "(" and s[i] != ")":
                    return False
        return len(stack) == 0