class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Need to perform Binary search for smallest element

        #If the input array is sorted in ascending order --> the array has been rotated n times

        #else elements from the end of array are moved ot beginning


        #At least ONE HALF of the array is always sorted
        l,r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            #Edge case: Sorted array
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
        
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
        