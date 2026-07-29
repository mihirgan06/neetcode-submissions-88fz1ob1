class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
            given an array of integers nums, nums[i] = max length of ajump towards the right from index i

            j <= nums[i]
            i + j < nums.length

            initially you are positioned at nums[0]
            return the min number of jumps to reach last position of the array

            nums = [2,4,1,1,1,1]
            start at index 0
            jump 1 to index 1, then jump 4 till the end of the array

            nums = [2,1,2,1,0]
            jump 1 from index 0 to index 3, then jump 2 to last index
            
        '''
        l, r = 0, 0
        num_jumps = 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            num_jumps += 1
        return num_jumps
            


        