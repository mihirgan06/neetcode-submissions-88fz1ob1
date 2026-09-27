class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            given a string s consisting of only upper case english characters and an integer k

            choose up to k characters of the string and replace with any other uppercase english characterReplacement
            after performing k replacements return the length of the longest substring with only one distinct character
            s = "XYYX", k = 2
            replace either the Xs or Ys with Ys or Xs
            s = "AAABABB", k = 1
            more As than Bs in a row so replace one B with an a
            Sliding window approach:
            - start l at 0
            - move r to the right 
            if s[l] == s[r] dont change any characters
            keep moving r right until we hit a diff character than switch into the predominant character whatever character increasing the longest increasing subsequence
            for every replacemnet increment replacements
            keep replacing until replacements = k

            s = "AAABABB", k = 1

            l = 0
            r = 0
            we shouod use a hashmap instead of set





        '''
        l = 0
        counts = defaultdict(int)
        maxFreq = 0
        max_window = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxFreq = max(maxFreq, counts[s[r]])
            num_replacements = (r - l + 1) - maxFreq
            if num_replacements > k:
                counts[s[l]] -= 1
                l += 1
            max_window = max(r - l + 1, max_window)
            
        return max_window


                


         



