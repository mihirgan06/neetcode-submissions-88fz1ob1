class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            given:
            - string s
            Return:
            - legnth of longest substring without duplicate characters

            Examples:

            s = "zxyzxyz"
            return 3
            start l at 0, keep moving r until we see a duplicate then move l if we find a duplicate to see if we can get a better substring




        '''

        l = 0
        seen = set()
        res = 0
        for r in range(len(s)):
            length = 0
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, len(seen))
        return res
