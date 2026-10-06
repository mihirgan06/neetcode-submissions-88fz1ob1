from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            Given: s1 and s2
            return true if s2 contains a permutation of s1

            false otherwsie

            Brute force: iterate with a fixed sliding window of s1
            compute hashmaps for bothj see if counts match if they do return true
            else keep moving iwndow and return fasle
        '''
        counts_s1 = defaultdict(int)
        
        if len(s1) > len(s2):
            return False
        window_size = len(s1)
        for i in range(len(s1)):
            counts_s1[s1[i]] += 1
        for r in range(len(s2) - window_size + 1):
            counts_s2 = defaultdict(int)
            for i in range(r, r + window_size):
                counts_s2[s2[i]] += 1
            if counts_s2 == counts_s1:
                return True
        return False
            
        