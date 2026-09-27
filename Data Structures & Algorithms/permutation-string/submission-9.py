class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            given two strings s1 and s2
            return true if s2 contains a permutation of s1 or false otherwise

            s1 = "abc", s2 = "lecabee"

            intial intuition:
            - iterate with a window of size s1
            - counts for s1 --> hashmap
            - abc 
            a = 1
            b = 1
            c = 1
            iterate through s2 with a window of size 3, for each window check if we jhabe a permutation of s1
            if we reach the end and dont find one then return false
        '''

        counts_s1 = defaultdict(int)
        for i in range(len(s1)):
            counts_s1[s1[i]] += 1
        
        window_size = len(s1)
        

        for r in range(len(s2) - window_size + 1):

            counts_s2 = defaultdict(int)
            for i in range(r, r + window_size):
                counts_s2[s2[i]] += 1
            if counts_s2 == counts_s1:
                return True
        return False


                    
