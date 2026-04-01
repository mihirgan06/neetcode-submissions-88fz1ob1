class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #given an array of distinct integers nums SORTED and a target, implenent a function to search for target within nums

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        
        return -1


        