from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        k = len(s1)

        need = defaultdict(int)
        window = defaultdict(int)

        for ch in s1:
            need[ch] += 1

        # first window
        for i in range(k):
            window[s2[i]] += 1
        #if we alr found our answer in the first window
        if window == need:
            return True

        # slide window
        for r in range(k, len(s2)):
            # incoming character
            window[s2[r]] += 1

            # outgoing character
            outgoing = s2[r - k]
            window[outgoing] -= 1

            # IMPORTANT with a normal/default dict
            if window[outgoing] == 0:
                del window[outgoing]

            if window == need:
                return True

        return False