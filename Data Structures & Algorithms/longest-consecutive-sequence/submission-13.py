class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Given an array of integers nums
            return the length of the longest consecutive elements that can be formec

            consecutive sequence is sequence of elements in which each element is exactly 1 greater than the previous elemnet

            len(set)
            use a set to track in o(1)
            we can convert the entire array of nums into a set
            check if x -1 in the set if x-1 is in the set it should be the start f the sequence

        '''
        nums_set = set(nums)
        best_sequence = 0

        for x in nums_set:
            if x-1 in nums_set:
                continue
            count = 1
            while x + 1 in nums_set:
                x += 1
                count += 1
            best_sequence = max(best_sequence, count)
        return best_sequence