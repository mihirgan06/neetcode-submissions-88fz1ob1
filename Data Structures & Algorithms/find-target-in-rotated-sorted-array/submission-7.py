class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            given an array of length n 
            sorted in ascending order
            it has now been rotated between 1 and n times


            nums = [1,2,3,4,5,6]

            rotated 1 time

            [6,1,2,3,4,5]
            2 times
            [5,6,1,2,3,4]
            3 times
            [4,5,6,1,2,3]
            4 times
            [3,4,5,6,1,2]

            target = 1
            l = 0
            r = 5
            mid = 2 --> 5
            if 5 is in the middle of the array
            then the array has been rotated 4 times
            so our target would be to the right --> search right side








            

            rotations move the last element to the first element

            binary search
            split array in half
            condition for searching ha
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] <= nums[r]:
                #this means the right side is sorted
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