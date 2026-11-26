class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            given: string s consisting of only uppercase english characters and an integer k
            choose up to k characters of the stirng and replace with any other uppercase english character
            s = "XYYX" k = 2
            length = 4
            X --> 2 Y --> 2 so replace either to get a max length of 4
            s = "AAABABB", k = 1

            A --> 4
            B --> 1
            replace that one B with an A to get a length of 5

            create a counts hashmap replace the character with the lower count in the window 

        '''
        counts = defaultdict(int)
        l = 0
        maxfreq = 0
        num_replacements = 0
        max_window = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxfreq = max(maxfreq, counts[s[r]])
            #while num replacements > k we shrink the window
            num_replacements = (r - l + 1) - maxfreq
            while num_replacements > k:
                counts[s[l]] -= 1
                l += 1
                num_replacements = (r - l + 1) - maxfreq
            max_window = max(r - l + 1, max_window)
            
        return max_window
                
            

        