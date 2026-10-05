class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            given an array of numbers SORTED in nondec order

            return the indices of two numbers [index1, index2] such that they add up to target and index1 < index2
            you mau not yse same elemtn twice


            since we know the input is sorted we can start two pointers left and right side

            if numbers[l] + numbers[r] > target --> we can move the right pointer down as we need our sum to go down
            if numbers[l] + numbers[r] < target --> we cna move left up as we need the sum to go up

            if we hit the target return the indices but ADD 1 sicne the array is 1-indiced
        '''
        l, r = 0, len(numbers) - 1
        res = []
        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum < target:
                l += 1
            elif two_sum > target:
                r -= 1
            else:
                res.append(l + 1)
                res.append(r + 1)
                return res

        