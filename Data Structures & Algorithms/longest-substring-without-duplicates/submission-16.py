class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            Given: string s, find the length of the longest substring without duplicate characters

            substring = contiguous sequence of characters within a string

            s = "zxyzxyz"
            output = 3
            xyz

            start l at z
            keep moving right 

            s = xxxx
            output = 1

            we want to use a sliding window + hash set approach
            if we reencounter a character ie its in our set
            we wanna shift our window
            else we wanna keep creating our window as thats the best length 



        '''
        l = 0
        seen = set()
        res = 0
        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])

                l += 1
            seen.add(s[r])
            res = max(res, len(seen))
        return res
            
                

        