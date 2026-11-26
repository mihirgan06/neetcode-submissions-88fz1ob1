class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            given: string s, find the longest substring without duplicate characters
            use a set to track duplicates
            if the character is already in our seen window we can move l to the right and remove s[l] from seen
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
            

            
        