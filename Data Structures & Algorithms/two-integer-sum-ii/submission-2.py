class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #given an array if onintegers nums (IN NON-DEC order)
        #return the indices of two nums such that thye add to target and index 1 < index 2

        #non dec --> Inc order
        #loop through array from right and left, checking if it equals the target
        l = 1
        r = len(numbers)
        res = []

        while l < r:

            if numbers[l - 1] + numbers[r - 1] == target:
                res.append(l)
                res.append(r)
                l += 1
                r -= 1
            elif numbers[l - 1] + numbers[r - 1] > target:
                r -= 1
            elif numbers[l - 1] + numbers[r - 1] < target:
                l += 1
        
        return res
        
            

        