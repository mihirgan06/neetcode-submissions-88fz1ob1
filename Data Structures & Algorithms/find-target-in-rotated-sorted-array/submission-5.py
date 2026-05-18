class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            We know rotation of n spots, moves the last n elements to the front of the array
            We cna use the same comparison we did with min in rotated sorted array but just do search

            Return -1 if we cant find target
            We have to actually emulate the rotations?

        '''

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] <= nums[r]:
                #the right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            

            else:
                #the left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        

        