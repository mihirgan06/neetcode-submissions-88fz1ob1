class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''
            given:
            - array of length n which was ORIGINALLY sorted in ascending order

            it has now been rotated between 1 and n itmes
            [1,2,3,4,5,6] 

            --> [3,4,5,6,1,2] if it was rotated 4 times.
            --> [1,2,3,4,5,6] if it was rotated 6 times.

            target:
            return the index of target within nums or -1 if its not present

            nums = [3,4,5,6,1,2], target = 1

            l = 0 r = 5
            mid = 2 --> 5
            we knwo target < mid --> target is ont he right side how do we know this
            we have easy access to the first and last element of the array
            we see nums[mid] > nums[r] so the target must be on the right side
            binary search the right side

            nums = [6,1,2,3,4,5], target = 1

            mid = 2
            num





        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            #the left side is sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            #right side is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1


        return - 1
