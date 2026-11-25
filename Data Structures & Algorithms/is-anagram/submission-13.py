class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            given two strings s and t
            return true if the two strings are anagrams otherwise return false

            two strings are anagrams if they contain same characters with each character appearing the same number of times


            open up two hashmaps counting number of characters in string s and t
            compare the counts for the two hashmaps
            if its the same then return true
            else false
        '''
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)
        if len(s) != len(t):
            return False

        for ch in s:
            counts_s[ch] += 1
        for ch in t:
            counts_t[ch] += 1
        
        #built the counts for the two maps

        for ch, count in counts_s.items():
            if counts_t[ch] != counts_s[ch]:
                return False
        return True
        