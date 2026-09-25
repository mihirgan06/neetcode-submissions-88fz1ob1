class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            given an integer array nums
            return all tripletes [nums[i], nums[j], nums[k]]
            nums[i] + nums[j] + nums[k] = target


            1. brute force
                Iterate through triple loop
                try all combinations and find sum compared to target

            2. why it is inefficient
                O(n)^3 cuz we iterate through elements 3 times
            3. pattern/data structure I'm using
                Two pointers with an anchor pointer
                start the anchor at nums[i] try left and right after anchor
                them move anchor after each element is tried
            4. what my variables mean

            5. why each pointer/hashmap decision is valid
                anchor poitner we lock down and try two poitner approach with each anchor
            6. time + space complexity

        '''
        nums.sort()
        
        res = []
        for i in range(len(nums)):
            anchor = nums[i]
            if i > 0 and anchor == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = anchor + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([anchor, nums[l], nums[r]])
                    l += 1
                    r-= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
        