class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
            Given: two strings s and t
            return the shortest substring of s such thate very character in t including duplicates is present int he substring
            s = "OUZODYXAZV", t = "XYZ"

            counts for t
            X --> 1
            Y --> 1
            Z --> 1
            


        '''
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
                #satisfied a condition
            #if we meet the overall condition
            while have == need:
                #update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                #pop from left of our window
                window[s[l]] -= 1
                #if s[l] is a NEEDED character and removing it is less than what we need
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("inf") else ""


        