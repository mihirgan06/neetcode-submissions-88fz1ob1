class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            given a string s, find the length of the longest substring without duplicates

            substring = continguous sequence of characters within a string

            EX: zxyzxyz
                longest substring = 3 (xyz)
                x - 1
                y = 1 
                z = 1

            
            EX:xxxx
                longest substring = 1 (x)
            Hashmap to count vlaues in a contiguous substring






        '''
        from collections import defaultdict
        l = 0
        counter = 0
        counts = defaultdict(int)

        for r in range(len(s)):
            #move r throught he array
            counts[s[r]] += 1
            #count for each cahracters
            while counts[s[r]] > 1:
                #we have already encountered the character
                counts[s[l]] -= 1
                l += 1
                
        return len(counts)





        
        