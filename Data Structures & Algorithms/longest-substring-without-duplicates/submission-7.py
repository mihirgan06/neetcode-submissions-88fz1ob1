class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            given a string s, fidn the length of the longest substring without duplicates

            substring is a contiguous sequence of characters within a string

            s = "zxyzxyz"
            3
            x,y,z
            we dont want duplicates



        '''
        l = 0
        best_sequence = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            
            best_sequence = max(len(seen), best_sequence)
        return best_sequence


            
            


        