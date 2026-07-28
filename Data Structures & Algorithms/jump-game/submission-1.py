class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
            Given an array nums where each element nums[i] indicates max junmp length at that position

            return true if you can reach the last index starting from 0 or false otherwsie

            nums = [1,2,0,1,0]
            true

            nums = [1,2,1,0,1]
            false
            jump from index 0 to 1, then to index 3 then we cant jump since nums[3] = 0

            O(n) time complexity

            starting at index 0, if index 0 we can return false

            [3,2,1,0,4]\

            at index 0 we cna make a jump of length 1,2, or 3
            no matter which option we do here we get to a deadend which is index 3 here (0)

            [2,3,1,1,4]
             s       G
             we know that second to last 1 can just reach the end
             now we know we just need ot get that 1
             the 1 before can reach that, so can we reach that from 0?
             the 3 before has an option of 1 to reach it
             and then the two has an option to reach that 3
             So we just keep shifting the goal post, if we are able to move that goal post to the start we know its odable

             This is O(n) we just shift the goal post max of n - 1 times


        '''

        if len(nums) == 1:
            return True
        if nums and nums[0] == 0:
            return False
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            #start at last index work till the beginning till we reach the first index
            if i + nums[i] >= goal:
                goal = i
        if goal > 0:
            return False
        return True