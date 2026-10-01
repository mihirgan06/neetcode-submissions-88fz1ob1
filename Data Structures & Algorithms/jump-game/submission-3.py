class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
            given an array nums, where each element nums[i]
            indicates your max jump length at that position
            return true if you can reach last index from 0 or false otherwise
            nums = [1,2,0,1,0]

            true
            jump from index 0 --> index 1 --> jump ot index 3 --> jump to index 4 good

            nums = [1,2,1,0,1]

            jump frm index 0 to index 1 to index 3
            false

            if the second to last index is 0 and we land on the second to last index then its false

            set the goal to the n - 1
                    goal
            [1,2,0,1,0]





        '''
        n = len(nums)
        goal = n - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            

        return goal == 0