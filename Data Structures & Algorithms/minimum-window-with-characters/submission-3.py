class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
            given two strings s and t, return the shortest substring of s such that 
            every character in t is present int he substring


            if such a substring doesn't exist

            s = "OUZODYXAZV", t = "XYZ"
            "YXAZ"
            we could have coutns for t, and then basically move a window and find the min that countains all the counts for t

            we update counts for t this is what we need

            then move throguh s, and check if we have everything if valid we can move l and see if we can shrink the window while still keeping everything
        '''
        countT = defaultdict(int)
        window = defaultdict(int)
        
        for i in range(len(t)):
            countT[t[i]] += 1
        l = 0
        need = len(countT)
        have = 0
        res = ""
        res_len = float("inf")
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res = s[l: r + 1]
                    res_len = r - l + 1
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res
                
            



            

        