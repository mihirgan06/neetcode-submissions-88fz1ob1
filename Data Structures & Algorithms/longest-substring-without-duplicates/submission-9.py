class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            given a string s:
            find the length of longest substring without duplicate characters
            s = "zxyzxyz"
            3

            xyz

            s = "xxxx"

            1

            iterate with a sliding window

            s = "zxyzxyz"
            l at 0 r at 0
            add z to seen
            nove r to 1
            now the window is zx
            add x to seen
            move r again
            y add to seen
            x



        '''
        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

                
            seen.add(s[r])
            res = max(len(seen), res)
        return res

