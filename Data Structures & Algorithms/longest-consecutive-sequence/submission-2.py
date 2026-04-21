class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        '''
            Given array of integers nums, return length of the longest consecutive sequence of elemnts

            Consecutive sequence elements which each element is greater than the previous by 1

            DO NOT need to be in order in the original array

            O(N*LogN) --> fucking sort that shi then do it but nah
            We can use a set to see if weve seen an elemnet, then comput ethe sum of the elemnent and add to set if not seen before

        '''
        my_set = set(nums)
        #create a set
        longest_seen = 0
        for num in my_set:
            if (num - 1) not in my_set:
                length = 1 #increment length if the smaller num is in the set t
                while (num + length) in my_set:
                    length += 1 #increment length
                longest_seen = max(length, longest_seen)
            
            
            
        

        return longest_seen
            
            


        