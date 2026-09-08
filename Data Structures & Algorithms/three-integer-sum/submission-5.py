class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            Given an integer array nums return the truplets [nums[i], numspj], nums[k]]

            nums[i] + nums[j] + nums[k] == 0

            nums = [-1,0,1,2,-1,-4]

            [[-1,-1,2], [-1,0,1]]
            nums.sort ==> [-4, -2, -1, -1, 0, 1]


            [[-1,-1, 2], [-1, 0, 1]]




        '''
        nums.sort()
        res = []
        anchor = 0


        for i in range(len(nums)):
            anchor = nums[i]
            l, r = i + 1, len(nums) - 1
            if i > 0 and anchor == nums[i - 1]:
                continue
            while l < r:
                three_sum = anchor + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([anchor, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                    
                






        