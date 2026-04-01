class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        #window size
        #we need to use the length of the substring as our sliding window
        #we can also integrate a freq table to count each letter in s2 so we know if its a permutation
        need = Counter(s1) 
        if len(s1) > len(s2):
            return False
        window = Counter(s2[0: k])
        for i in range(len(s2) - k + 1):
            if window == need:
                return True
            if i + k < len(s2):
                window[s2[i]] -= 1
                window[s2[i + k]] += 1 
            #we slide by k not by 1
        return False
        
        

        
        