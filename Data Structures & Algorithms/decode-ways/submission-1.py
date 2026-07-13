class Solution:
    def numDecodings(self, s: str) -> int:
        '''
            a string w uppercase english characters can be encoded into a numebr
            A = 1
            B = 2
            Z = 26



            decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping
            JAB = 10 1 2
            JL = 10 12

            s contianing only digits, return number of ways to decode it

            s = "12" --> 2 
            12 = AB or L (12)
            

            Top down:
                - we want to try each numebr converting it into a string

            '''
        cache = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                #we finished this entire path
                return 1
            if int(s[i]) == 0:
                #a single char as 0 cannot be a valid path on its own
                return 0
            ways = 0
            if cache[i] != -1:
                return cache[i]

            ways += dfs(i +1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)
            cache[i] = ways
            return cache[i]
        return dfs(0)

            
            


