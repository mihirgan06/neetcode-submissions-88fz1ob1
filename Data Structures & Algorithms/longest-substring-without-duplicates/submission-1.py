class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''My approach:
        we keep a set to keep track of the fact that theres no duplicates
        if the char were on rn is alr in the set, we eed to move the l pointer forward
        Else we just keep moving r forward and adding the next character in the string to the set
        '''
        l, r = 0, 0
        my_set = set()
        res = 0
        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[r])
            res = max(res, r - l + 1)
        return res
            
            
