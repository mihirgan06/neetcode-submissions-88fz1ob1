class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
            Given a string s, and a dictionary woirdDict, 
            return True if s can be segmnented into a space sperated sequence of dictionary words

            s = "neetcode, wordDict = neet code
            true

            s = "applepenapple", wordDict = ["apple","pen","ape"]
            true


            
            Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
            car fails so false
        
            each phrase in worddict has to be a contiguous substring of s


        '''
        cache = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return True
            if cache[i] != -1:
                return cache[i]
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if dfs(i + len(word)):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        return dfs(0)
                
                


