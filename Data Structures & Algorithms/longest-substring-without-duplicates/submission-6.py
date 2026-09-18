class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leng = len(s)
        seen = set()
        ans = 0
        l = 0
        for r in range(leng):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            ans = max(ans, len(seen))
        return ans