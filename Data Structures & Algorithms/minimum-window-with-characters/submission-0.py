class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
            Input: two strings, not guaranteed to be just a - z, could be A-Z could also be duplicates

            NOT 26 fixed, use defaultdict
            First edge case: len(t) > len(s) --> return "" (empty string)
            every character of t has to be in s --> so matches again
            BUT we want to find the minimum possible window where this is the case
            








        '''
        from collections import defaultdict
        #edge case len(t) > len(s)
        if len(t) > len(s):
            return ""
        tcount = defaultdict(int)
        scount = defaultdict(int)

        #rememebr ur iterating w ch not with i so you dont do len(range)

        for ch in t:
            tcount[ch] += 1
        #count the occurances for each ch in tcount
        matches = 0
        l = 0
        #r as a pointer

        #unique characters

        have = 0 #the number currently satisfied in the window

        need = len(tcount) #the number we need

        #b
        for r in range(len(s)):
            #update s count count
            #start the sliding window with the right pointer
            scount[s[r]] += 1
            #update count for r
            #adds s[r] to the window 
            res = [-1, -1]
            resLen = float('inf')

            if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                have += 1
            while have == need:
                #while the current window is valid
                scount[s[l]] -= 1
                #if the character is already in tcount and scount for the cahracter in s is less than tcount
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
            l, r = res
            return s[l: r + 1] if resLen != float('inf')  else ""

        

        


            







        

        
        



