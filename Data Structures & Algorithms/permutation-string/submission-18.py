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
            However in htis case we are recomputing the permutation for every fixed window


            How can we do better?


            we can calculate for the first window
            then move forward from there
        '''
        if len(s1) > len(s2):
            return False
        counts_s1 = defaultdict(int)
        counts_s2 = defaultdict(int)
        for i in range(len(s1)):
            counts_s1[s1[i]] += 1
        k = len(s1)
        for i in range(k):
           counts_s2[s2[i]] += 1
        if counts_s1 == counts_s2:
            return True
        for r in range(k, len(s2)):
            counts_s2[s2[r]] += 1
            outgoing = s2[r - k]
            counts_s2[outgoing] -= 1
            if counts_s2[outgoing] == 0:
                del counts_s2[outgoing]
            if counts_s1 == counts_s2:
                return True
        return False
             
            
        