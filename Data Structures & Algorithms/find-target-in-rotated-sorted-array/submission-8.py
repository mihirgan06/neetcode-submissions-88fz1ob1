class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            given ana rray of length n in ascending order

            it has now been rotated between 1 and n times
            [1,2,3,4,5,6]

            [3,4,5,6,1,2] --> rotated 4 times
            rotation 1 --> [6,1,2,3,4,5]
            rotation 2 --> [5,6,1,2,3,4]
            rotation 3 --> [4,5,6,1,2,3]
            rotation 4 --> [3,4,5,6,1,2]

            given the sorted array nums and an integer target, return the index of target within nums or -1 if not present


            nums = [3,4,5,6,1,2], target = 1

            when we compute mid we can tell which side to search based on the rotations

            nums[mid] = 5
            how do we know which side to search
            target = 1 < 5
            we can compare the end of the array to the mid and if its less we know its been rotated and we can search the appropriate side







        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            #left side is sorted
            if nums[l] <= nums[mid]:
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
        return -1

            






        