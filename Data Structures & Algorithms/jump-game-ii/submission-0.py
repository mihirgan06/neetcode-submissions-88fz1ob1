class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
            Given an array of nums, where nums[i] represents the max length of jump right form index i

            You can jump to any index i + j
            j <= nums[i]
            and i + j < nums.length
            return the min number of jumps to reach the last position in the array (nums.length - 1)


            nums = [2,4,1,1,1,1]
            BFS + Greedy
                1.  2
            [2,3,1,1,4]
            From 2 we cna get to 3 or 1
            from the 3 we can get to 1, but its redundant, as we can already get there
            we can also get to the next 1, but we can ALSO reach the destination!
            if we get to the 4 we found the minimum



        '''
        l, r = 0, 0
        num_jumps = 0


        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            num_jumps += 1
        return num_jumps
        '''
        if len(nums) == 1:
            return 1
        if nums and nums[0] == 0:
            return 0
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal and goal <= nums[i]:
                goal = i
                num_jumps += 1
        if goal > 0:
            return 0 #not possible
        return num_jumps
        
        '''

        