class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            given an array of integers numbers sorted in nondec order

            return the indices (1-indexed) of two numbers, [index1, index2] such that they add up to a given target and index1 < index2

            [1,2,3,4] target = 3
            [1,2]

            normally would be indices 0, 1 but since its 1 indexed just add 1 to both indices

            always one solution so logic is p easy

            start two pointers
            if the sum of the two pointers > target move right to the left
            if the sum of the two pointers < target move left to the right
            once we find the solution return the two indices + 1
        '''
        l, r = 0, len(numbers) - 1
        while l < r:
            two_sum = numbers[l] + numbers[r]

            if two_sum < target:
                l += 1
            elif two_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        