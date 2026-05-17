class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #array of nums in sorted ascending order and target

        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if target < nums[mid]:
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            elif target == nums[mid]:
                return mid
        return -1

        