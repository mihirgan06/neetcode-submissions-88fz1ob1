class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
            given a string s and a dictionary of words wordDict
            return true if s can be segmented into a space seperated sequence fo dictionary words
            s = "neetcode", wordDict = ["neet","code"]

            true


            s = "applepenapple", wordDict = ["apple","pen","ape"]

            dp should be a boolean array
            dp[i] = True if the first i characters of s
        can be split entirely into words from wordDict



            
        '''
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True #we can make a string of 0 from nothing


        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in words:
                    dp[i] = True
        return dp[len(s)]

        