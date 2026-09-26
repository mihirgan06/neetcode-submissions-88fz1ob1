class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            given a string s, find the length of the longest substring without duplicate characters

            substring is a contiguous sequence of characters within a string

            s = "zxyzxyz"

            output = 3

            xyz

            s = "xxxx"

            1 
            cant have duplicates, so if we have a duplicate we remove the cleft chacter from the set and then shift the window to the right





        '''
        l = 0
        seen = set()
        best_sequence = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best_sequence = max(len(seen), best_sequence)
        return best_sequence



        