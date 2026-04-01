class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #goal O(N) time

        '''
        Consecutive sequence -> sequence of elements in which each element is exactly 1 greater than the previous element
        We can sort the elements -> now its in order
        However, this owuld be O(n log n)
        

        We can utilize a set
        Put all te numbers into set
        Check whether a number is the start of a set
        Only expand sequences when you find a set
        Count forward (x + 1, x + 2, ...) while they exit
        '''
        
        numSet = set(nums)
        #need to initialize longest as a globla variable
        longest = 0 #longest length weve seen so far

        for num in numSet:
            if (num - 1) not in numSet:
                current = num
                length = 1
                while current + 1 in numSet:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest

