class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        thoughts:
        our goal is to get to 0 with all possible triplets
        we can do two pointers 


        '''
        res = []

        nums.sort()
        #needed well have a small pointer and a large pointer
        for i, anchor in enumerate(nums):
            if anchor > 0:
                break
            
            if i > 0 and anchor == nums[i - 1]:
                continue
        
        
            l = i + 1
            r = len(nums) - 1
            while l < r:
                int_sum = anchor + nums[l] + nums[r]
                if int_sum > 0:
                    #we neeed to make our runnng sum greater so move left to the right
                    r -= 1
                elif int_sum < 0:
                    l += 1
                

                else:
                    res.append([anchor, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res



        