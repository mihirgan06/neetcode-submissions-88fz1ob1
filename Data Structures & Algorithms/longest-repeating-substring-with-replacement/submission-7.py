class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            Given: string s: only uppercase english characters and integer k
            you may choose up to k characters of the string and replace them with any otehr uppercase letter


            after performing at most k replaements return the length of the longest substring which contains only one distinct character

            Approach:
            - counts of each character
            s = "XYYX", k = 2

            X --> 2, Y --> 2
            s = "AAABABB", k = 1

            A --> 4
            B --> 3
            1 replacemnet wed want to replace the B
            Iterate with a sliding window
            when we see a new character increment the count for it
            We should shrink the

        '''
        counts = defaultdict(int)
        maxfreq = 0

        
        l = 0
        max_length = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxfreq = max(maxfreq, counts[s[r]])
            while (r - l + 1) - maxfreq > k:
                counts[s[l]] -= 1
                l += 1
            max_length = max(r - l + 1, max_length)
        return max_length    
                
            

            



        

        