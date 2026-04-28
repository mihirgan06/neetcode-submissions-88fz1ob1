class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
            Attempting matches algorithm:
            Matches = number of indices where s1Count[i] == s2Count[i]

            Total of 26 matches possible, if all 26 match then: matches == 26

            SETUP:
                s1Count --> counts for s1
                s2Count --> counts of first window in s2


        '''
        #NO HASHMAPS
        #create just two arrays for the every possible letter, 26 each
        #edge case the two array sizes
        if len(s1) > len(s2):
            return False
        
        k = len(s1)

        s1counts, s2counts = [0] * 26, [0] * 26


        for i in range(len(s1)):
            s1counts[ord(s1[i]) - ord('a')] += 1
            s2counts[ord(s2[i]) - ord('a')] += 1
        matches = 0
        #initialize the count of matches to 0
        for i in range(26): #max is that there are 26 matches
            if s1counts[i] == s2counts[i]:
                matches += 1
        
        l = 0
        for r in range(k, len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a') #compute index for the right index this is how we add a character to the window
            s2counts[index] += 1 #add a chatacter to window

            if s1counts[index] == s2counts[index]:
                matches += 1
            elif s1counts[index] + 1 == s2counts[index]:
                matches -= 1
            index = ord(s2[l]) - ord('a')
            s2counts[index] -= 1
            if s1counts[index] == s2counts[index]:
                matches += 1
            elif s1counts[index] - 1 == s2counts[index]:
                matches -= 1
            l += 1
        return matches == 26

            
        
        
                







        