class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            given 2 strings s1 and s2
            return true if s2 has a perm of s1 false otehrwise
            Input: s1 = "abc", s2 = "lecabee"
            Output: true

            Input: s1 = "abc", s2 = "lecaabee"
            Output: false





            
        '''
        if len(s1) > len(s2):
            return False

        s1_counts = [0] * 26
        window_count = [0] * 26

        window_size = len(s1)
        #build counts for s1 and the first window of s2
        for i in range(window_size):
            s1_counts[ord(s1[i]) - ord('a')] += 1 
            window_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_counts == window_count:
            return True
        l = 0

        for r in range(window_size, len(s2)):
            window_count[ord(s2[r]) - ord('a')] += 1

            window_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if s1_counts == window_count:
                return True
        return False

        

