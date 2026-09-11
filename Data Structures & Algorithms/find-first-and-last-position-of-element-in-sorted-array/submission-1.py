class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
            given an array of integers nums sorted
            find starting and ending posiiton of a given target value

            If we dont find target return [-1, -1]

            nums = [5,7,7,8,8,10], target = 8

            we find 8 and then the range for where 8 is

            nums = [1], target = 1

            return [0,0]



            binary search for the target and then return the range the target its in


        '''

        l, r = 0, len(nums) - 1
        first, last = -1, -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                first = mid
                r = mid - 1
 
            
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if first == -1:
            return [-1, -1]

        # RESET binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                last = mid
                l = mid + 1
                
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return [first, last]
            




        