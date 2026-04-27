class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            given two strings s1 and s2
            Return true if s2 countains a permutation of s1
            FALSE otherwise

            permutation of s1 exists as a substring of s2

            Return true if so
            else false

            The only thing we care aboiut is ocunts


            EX: abc, lecabee
            True because cab is a permutation of abc
            Same amout of counts for c, a, and b

            O(N)
        
        Brute Force:
            just use a map for the counts of every letter in s1
            then compare and make sure the permutation counts match

        Optimal:
            Fixed window size len(s1), move through string and compare counts within each one

        '''
        from collections import defaultdict
        counts = defaultdict(int)
        counts2 = defaultdict(int)
        for ch in s1:
            counts[ch] += 1
        
        l = 0
        for r in range(len(s2)):
            #iterate using the window
            counts2[s2[r]] += 1

            if r - l + 1 > len(s1):
                l += 1
                #shrink window
            if r - l + 1 == len(s1):
                #window size = len(s1) --> compare the counts
                return True
        return False
            





        