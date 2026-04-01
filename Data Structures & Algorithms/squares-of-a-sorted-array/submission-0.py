class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #given array in non-dec order
        #return array of SQUARES of each number SORTED in non dec order

        left = 0 #point it to the left most index

        right = len(nums) - 1 #points to right most index
        res = []

        while left <= right:
            #if the left index > right index append the square of left
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1 #move left right
            
            else:
                #if not append sqare pf the right index
                res.append(nums[right] ** 2)
                right -= 1 #move right left
        res.reverse()

        return res
            




        