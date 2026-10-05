class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
            Given: nums
            each element nums[i] = max jump length at that position
            return t/f if you can or cant reach last index starting from 0
            goal is nums[len(nums) - 1]
            we can start from the right and see if we can reach the goal and move the goal back to i
        '''
        goal = len(nums) - 1

        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
                
        