class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Given:
        nums consisting of n elements --> each eleemnt is an integer representing color

        0 = red
        1 = white
        2 = blue

        sort the array in place
        elements of the same color are grouped together
        NO build in sorting

        O(n) solution:
        2 pointers and swap
        if we see a 2 we can swap with the 0

        we want to swap if we see a 0 on the right side and 2 on the left side

        walkthrough example

        [1,0,1,2]

        l = 0 r = 3
        nums[l] = 1, nums[r] = 2
        move r backward
        nums[r]] = 1





        """
        l, r = 0, len(nums) - 1
        i =0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1
        
                
            

            
            


        