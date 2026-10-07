class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            Given: String s find the length of the longest substring without duplicate characters
            Sliding window approach:
            s = "zxyzxyz"
            Approach:
            - initialize a set for seen
            - we want to shrink the window when a number is in seen
            - so like if nums[r] is in seen we can shrink window from the left and remove nums[l] from seen
            - the longest substring is between the size of the current window and the set length


        '''
        seen = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_length = max(len(seen), max_length)
        return max_length