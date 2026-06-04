class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            The total number of parentheses = 2 * n --> Base case
            #opens must match #closed no matter what

            if we have more opens then closed add closed, if we have less openms then n just add parenthsesis

        '''
        res = []
        path = []
        def backtrack(num_open, num_close):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return res
            
            if num_open < n:
                #we have too little opens
                path.append("(")
                backtrack(num_open + 1, num_close)
                path.pop() #if we dont append

            if num_close < num_open:
                path.append(")")
                backtrack(num_open, num_close + 1)
                path.pop()
        backtrack(0, 0)
        return res
        