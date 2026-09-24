class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed

            Consecutive sequence is sequence in which each element is exactly 1 greater than prev

            nums = [2,20,4,10,3,4,5]
            return 4 --> 2, 3, 4, 5


            nums = [0,3,2,5,4,6,1,1]

            return 7 --> 0, 1, 2, 3, 4, 5, 6

            elements do not need to be in order in the original array

            we could turn the entire array into a set
            and then choose the next elemnet in O(1)




        '''
        set_nums = set()
        max_count = 0
        for i in range(len(nums)):
            set_nums.add(nums[i])

        for x in set_nums:
            if x - 1 in set_nums:               
                continue
            count = 1

            while x + 1 in set_nums:
                x += 1
                count += 1
            max_count = max(count, max_count)
        return max_count
                

        



        