class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            given an array of integers in non-dec order
            indices 1-indexed of two numbers [index1, index2] add to target

            index 1 < index2

            2 pointer:

            nums = [1,2,3,4], target = 3
            L at 1, R at 4
            fi the sum > target mopve the right pointer left

            if the sum < target move the left pointer right


            egdge case: 1-indexed not 0-indexed
        '''

        l, r = 0, len(numbers) - 1
        while l < r:
            int_sum = numbers[l] + numbers[r]

            if int_sum < target:
                l += 1
            elif int_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []