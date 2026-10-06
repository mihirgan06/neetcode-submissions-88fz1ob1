class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Given: array nums, 
            Return: length of longest consecutive sequence of elements that can be formed

            consecutive sequence = sequence of elements in which each element is exactly 1 greater than the prev element

            nums = [2,20,4,10,3,4,5]
            4 --> 2,3,4,5
            nums = [0,3,2,5,4,6,1,1]
            O(n) so we cant sort
            we can use a set for O(1) lookups
            convert the entire array into a set

            for every x in the set, look for x + 1, if we see x -1 skip that iteration
            we only wnat to start for x



        '''
        set_nums = set(nums)
        best_sequence = 0
        count = 0
        for x in set_nums:
            if x - 1 in set_nums:
                continue
            count = 1
            while (x+1) in set_nums:
                x += 1
                count += 1
    
            best_sequence = max(count, best_sequence)
        return best_sequence

            
            
            
        