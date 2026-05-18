class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
            Trivial we legit just call min
            THis one doesnt seem too bad
            The number of rotations (n) moves the last n elements to the front of the array
            If the number of rotations = number of elements in the array reproduces the original array
            We cant just do typical binary search as the array is not alr sorted in asc

        '''
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            #get mid, compare mid to the right
            if nums[mid] <= nums[r]:
                #if nums mid < nums[r]
                r = mid
            else:
                l = mid + 1
        return nums[l]

        
        