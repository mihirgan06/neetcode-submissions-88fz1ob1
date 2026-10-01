class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
            given a string s, and a dictionary of strings wordDict
            return true if s can be segmented into a space-seperated of dictionary words


            s = "neetcode", wordDict = ["neet","code"]
            true we can split neetcode into neet and code


            s = "applepenapple", wordDict = ["apple","pen","ape"]

            true --> we can reuse words and we dont have to use all the words
            every character in s must belong to some chosen dictionary word
            dp[i] = can the first i characters of s be fully segmented into dictionary words?




        '''
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True #empty string can be created into a word
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in words:
                    dp[i] = True
        return dp[len(s)]
                



        