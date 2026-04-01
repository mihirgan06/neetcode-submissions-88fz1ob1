class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #given an integer array nums, find triplets where nums[i] + nums[j] + nums[k] == 0


        #return the triplets in seperate arrays

        #start a pointer at left end, right end
#have a pointer at the middle
        #keep one pointer fixed at the middle, and then two pointer approach check for the sum using the 3 pointers


        nums.sort()
        res = []
        for i in range(len(nums)):
            anchor = nums[i]
            l = i + 1
            r = len(nums) - 1
            if i > 0 and anchor == nums[i - 1]:
                continue
            while l < r:
                    
                three_sum = nums[l] + anchor + nums[r]
                if three_sum == 0:
                    res.append([nums[l], anchor, nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                
                
        return res
        