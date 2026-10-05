class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            Given:
            - 2 strings s1 and s2
            return:
            boolean true if s2 contains a permutation of s1 false otherwise

            if len(s1) > len(s2) return false 

            permutations contain the same counts for each character in the window


            fixed sliding window of size s1
        '''
        if len(s1) > len(s2):
            return False
        window_size = len(s1)
        counts_s1 = defaultdict(int)
        for i in range(len(s1)):
            counts_s1[s1[i]] += 1
        for r in range(len(s2) - window_size + 1):
            counts_s2 = defaultdict(int)
            for i in range(r, r + window_size):
                counts_s2[s2[i]] += 1
            if counts_s2 == counts_s1:
                return True
        return False
        

        

        