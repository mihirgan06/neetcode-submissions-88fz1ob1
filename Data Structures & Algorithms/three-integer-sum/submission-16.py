class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            Given: nums, return all the triplets [nums[i]], nums[j], nums[k] where the three elements == 0
            nums = [-1,0,1,2,-1,-4]
            [[-1, -1, 2], [-1, 0, 1]]
            we dont want duplicate TRIPLETS
            but within our triplets we can reuse the same element
            triplets must be unique thouigh

            Goal: O(n^2)
            we can have two pointers ocmpute two sum but have ana dditional anchor pointer
            we can start the anchor at the first index and then try every combo for that pointer
            then move the anchor

            start by sorting nums so we can hvae clean logic for moving pointers

        '''
        res = []
        nums.sort()

        for i in range(len(nums)):
            anchor = nums[i]
            l = i + 1
            r = len(nums) - 1
            if i > 0 and anchor == nums[i - 1]:
                continue
            while l < r:
                three_sum = nums[l] + nums[r] + anchor
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([anchor, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
                