from collections import Counter
class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        #we have the counts of each letter in string, we want torep
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            #can also be done with counter
            #res = size of the window
            res = max(res, r - l +1)
        return res

        



        