class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            given an array of integers numbers sorted in non-dec order


            return the indices (1-indexed !)

            of two numbers such that they add up to a given target
        '''
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
            



        