class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            given two strings s and t, return true if the two strings are anagrams of each other

            2 strings are anagrams if they have the same characters with each character appearing same numbner of times

            approach:
            - to be an anagram: same characters with each character appearing same number of times

            - so length of the two strings should be the same
            - 2 hashmaps one for s one for t then comapre counts


        '''

        if len(s) != len(t):
            return False
        s_hashmap = defaultdict(int)
        t_hashmap = defaultdict(int)
        #compute coutns for s and t then compare
        for ch in s:
            s_hashmap[ch] += 1

        for ch in t:
            t_hashmap[ch] += 1


        for ch, count in t_hashmap.items():
            if t_hashmap[ch] != s_hashmap[ch]:
                return False
        return True
                



        