class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            given an array of length n which was originally sorted in ascending order

            nums = [3,4,5,6,1,2] rotated 4 times

            find the min element of this array

            recognize which half is sorted, and search for min in that half if we cant find it search the other half
            nums = [3,4,5,6,1,2]

            l = 0
            r = 5
            mid = 2
            if nums[l] < nums[mid]




        '''
        
        res = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res

        
                

