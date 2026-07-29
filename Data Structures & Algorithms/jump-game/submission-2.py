class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
            Given an integer array nums where each element nums[i] = max jump length
            Return true if you can reach last index from index 0
            false otherwise

            nums = [1,2,0,1,0]

            true
            At each spot you can do anything in the range of the jump

            1 --> 2 --> 1 --> reach last index

            nums = [1,2,1,0,1]
            false
            no way to reach last index
            move the goal post, starts at the last index

        '''
        goal = len(nums) - 1
        if len(nums) == 1:
            return True
            
        if nums and nums[0] == 0:
            return False
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal > 0:
            return False
        return True
            


        