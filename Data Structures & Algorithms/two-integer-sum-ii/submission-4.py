class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            Given array of nums in non-dec order
            1-indiced of two numbers [idx 1, index 2]

            Add up to target, 1 < 2


            O(N) time

            Approach:
                Legit just iterate through array while l <= r
                Since nondec we know which order to move pointers based on the sum of the values
                


                How to deal with the 1 indexed:

        '''
        l = 0
        r = len(numbers) - 1
        res = []
        while l < r:
            int_sum = numbers[l] + numbers[r]
            if int_sum > target:
                r -= 1
            elif int_sum < target:
                l += 1
            #move l or r based on the value of the sum
            else: #if the sum = target
                res.append(l + 1)
                res.append(r + 1)
                l += 1
                r -= 1

        return res
            