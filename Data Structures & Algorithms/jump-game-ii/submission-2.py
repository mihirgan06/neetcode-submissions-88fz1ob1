class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
            you are given an array of integers nums where nums[i] represents the max length of a jump towards the right from index i
            you can jump to any index i + j where:
            j <= nums[i]
            return the min number of jumps to reach the last position in the array (nums.length - 1)
            the greedy choice is to take the min number of jumps by taking the largest jump possible
            [2,3,1,1,4]

            start at position 0
            we can either take jump of length 1 and length 2

            take jump of 1
            jup straight to 4
            at 2 we have 2 decisions we can juimp to 3 or to 1

            [2,3,1,1,4]
            0 jumps to reach 2
            1 jump to reach 3 or 1
            2 jumps to reach 1 or 4
            the boundaries are determined by the max we can jump from our section and the min we can jump from our boundaries
            
        '''
        res = 0
        l, r = 0, 0
        #while right pointer is < last index keep incrementing our result
        while r < len(nums) - 1:
            farthest = 0
            #go through our window we want to determine who can jump the farthesrt
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res




            

