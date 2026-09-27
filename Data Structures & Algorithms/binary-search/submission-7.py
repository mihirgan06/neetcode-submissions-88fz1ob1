class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            given an array of distinct integers nums sorted in ascending order and an integer target
            implement a function to search for target within numsk


            Binary search
            l and r pointers
            mid if the target is on right side move l to mid + 1
            if the target is on left side move r to left of mid (mid - 1)
        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            #search right side
            elif target > nums[mid]:
                l = mid + 1
            #search left side
            else:
                r = mid - 1
        return -1