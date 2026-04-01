class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #given two strings s and t, return true of the twpo strings are anagrams else return false

        #anagrams must have the same NUMBER of characters and same exact characters
        if len(s) != len(t):
            return False
        
        freq = {}

        for i, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            #counts the number of each characters in s

        for i, ch in enumerate(t):
            if ch not in freq:
                return False
            freq[ch] = freq.get(ch, 0) - 1
            if freq.get(ch) < 0:
                return False;
        #we subtract the count from s for every shared character in s

        return True

        
        