from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            given 2 strings s1 and s2
            return true if s2 contains a permutation of s1 or false otherwise


            create a counts array for s1 and then the first window of s2
            then move the winodw through s2
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