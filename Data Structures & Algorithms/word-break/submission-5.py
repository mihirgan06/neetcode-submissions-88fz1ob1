class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
            Given: string s, and dictionary of strings wordDict

            return: true if s can be segmented into a space-separated sequence of dictionary words
            you dont have to use all the words and you can repeat words from the dict
            s = "neetcode", wordDict = ["neet","code"]

            dp[i] = whetehr or not we can split the first i character of the string into words of the dictionary




        '''
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    
        return dp[len(s)]