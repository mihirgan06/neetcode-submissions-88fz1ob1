class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
            Given string s, split the string into substrings where each string is a palindrome

            s = aab
            --> [[a, a, b], [aa, b]]
        '''
        res = []
        path = []
        def is_palindrome(piece):
            l, r = 0, len(piece) - 1
            while l < r:
                if piece[l] != piece[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        def backtrack(start):
            if start == len(s): #we used/cut the entire string so the path is a valid aprtition
                res.append(path[:])
                return
            for ch in range(start, len(s)):
                piece = s[start: ch + 1] #inclusive slice of s from start to end
                if is_palindrome(piece):
                    path.append(piece)
                    backtrack(ch + 1)
                    path.pop()

        backtrack(0)
        return res

        


        