class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #planned approach:
            #frewquency map for letters in string 1
            #sliding window on string 2, make sure the counts of the chars in string 1 exist in string 2
            
        freq = {}
        for i, ch in enumerate(s1):
            freq[ch] = freq.get(ch, 0) + 1
            #count the frequency of eqch letter character in string 1

        window = len(s1)

        left = 0
        freq2 = {}
        for right in range(len(s2)):
            ch = s2[right]
            freq2[ch] = freq2.get(ch, 0) + 1
            
            if right - left + 1 > window:
                #removing s2[left] from the window
                #the window gets too large so we must remove the leftmost character
                #also we must move left forward by 1, thus sliding the window one step right
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if right - left + 1 == window and freq == freq2:
                return True
        
        return False
            




        

        