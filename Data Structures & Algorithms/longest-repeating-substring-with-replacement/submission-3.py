class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            given string only uppercase, and integer k
            choose up to k chars of string and replace with any uppercase English cahracter

            After k replacements return length of longest substring



            EX:
                XYYX, k = 2
                We can do two replacements of the Ys with Xs or Xs with Ys
                then return length of the updated string

            EX:
                AAABABB, k = 1
                Relace the B with an A --> get 5

            
            AIM O(N) 

            Intuition:
                Similarly we need a hashmap to count unique chars
                BUT rather than just shrinking the window, we need to replace the nonunique character with whatever amkes the string the longest

                do the same max string thing -
                LIGHT WORK
        '''
        from collections import defaultdict
        l = 0
        max_freq = 0
        counts = defaultdict(int)
        max_length = 0

        for r in range(len(s)):
            #increment counts for each window
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])

            
                #if we encounter a non-unique character, we dont shrink window
                #we actually replace that character with whatever the rest of the string is

               #we dont want to modify count rather the string
               #nvm we cant  mutate strings, and either way it doesnt work
            while r - l + 1 - max_freq > k:#window size - max_freq
                #while the window size - the appearance of the most frequent char
                #left side is the number of unique chars, as long as thats > k
                counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

               
               

