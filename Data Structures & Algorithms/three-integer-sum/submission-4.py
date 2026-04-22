class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            Given nums, return [nums[i], nums[j], nums[k]]
            nums[i] + nums[j] + nums[k] == 0, i != j != k

            2 pointer, obv jsut kinda do similar to 2 sum

            fix a pointer

            You need O(N^2) time, 
            you can do two pointers in a single pass, so you need that second pass for the additional pointer



        '''

        nums.sort()
        
        
        #intuition im aware you need an anchor pointer
        #probably you need ot place this anchor for whatever the compliment is when adding the two pointers

        res = []
        
        for i in range(len(nums)):
            
            anchor = nums[i]
            l = i + 1
            r = len(nums) - 1
            #how we deal with duplicates
            if i > 0 and anchor == nums[i - 1]:
                continue
            while l < r:
                three_sum = anchor + nums[l] + nums[r]
                if three_sum > 0:
                    #we need to check if theres a complement for this
                    #we dont move r unless theres a compleemnt
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], anchor])
                    r-= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res




            
            
        