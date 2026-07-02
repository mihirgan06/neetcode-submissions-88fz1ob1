class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        # Case 1: exclude last, use houses 0 to n-2
        dp1 = [0] * (n + 1)
        dp1[1] = nums[0]

        for i in range(2, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i - 1])

        case1 = dp1[n - 1]

        # Case 2: exclude first, use houses 1 to n-1
        dp2 = [0] * (n + 1)
        dp2[1] = nums[1]

        for i in range(2, n):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        case2 = dp2[n - 1]

        return max(case1, case2)