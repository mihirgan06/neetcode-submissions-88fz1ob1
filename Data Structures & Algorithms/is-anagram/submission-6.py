class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            Given two strings s and t, return true if the two strings are anagrams
            Else return false
        '''
        from collections import defaultdict
        if len(s) != len(t):
            return False
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)

        for ch in s:
            counts_s[ch] += 1
        for ch in t:
            counts_t[ch] += 1
        for key in counts_s.keys():
            if counts_s[key] != counts_t[key]:
                return False
            
        return True

            
        

        