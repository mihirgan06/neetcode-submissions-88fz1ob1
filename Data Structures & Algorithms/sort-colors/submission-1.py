class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """

        iterate thru nums
        - 0 --> sort to left
        - 1 --> do nothing, naturally end up in middle
        - 2 --> sort to right

        i
        L         R
        2 0 2 1 1 0

        """
        L, R = 0, len(nums)-1 # BOUNDARY POINTERS
        i = 0

        while i <= R:
            if nums[i] == 0: # swap left
                nums[i], nums[L] = nums[L], nums[i]
                L += 1
            elif nums[i] == 2:
                nums[i], nums[R] = nums[R], nums[i]
                r -= 1
                i -= 1 # offset to left to reconsider newly swapped elem
            i += 1
        
        return None