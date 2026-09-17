class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            L = i + 1
            R = length-1
            while L < R:
                if a + nums[L] + nums[R] < 0:
                    L += 1
                elif a + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                    
        return res