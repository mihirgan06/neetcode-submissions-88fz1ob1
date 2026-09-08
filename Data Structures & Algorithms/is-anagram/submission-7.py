class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            given two strings s and tm return true if ths two strings are anagrams else
            reutrn faslse
            same cahracters with each char appearing the same number of times

            s = racecar
            t = carrace
            true

            s = jar, t = jam --> false


            anagram if same characters with each cahracter same number of times

            we want to first compare length

            - then count the numebr of appearances of each cahracter
            - then iterate throught he maps looking for if they dont match
            - return false if at the end of iteration they dont mathc
        '''
        if len(s) != len(t):
            return False
        s_count = defaultdict(int)
        t_count = defaultdict(int)
        for ch in s:
            s_count[ch] += 1
        for ch in t:
            t_count[ch] += 1
        

        for key, value in t_count.items():
            if s_count[key] != t_count[key]:
                return False
        return True


        







        