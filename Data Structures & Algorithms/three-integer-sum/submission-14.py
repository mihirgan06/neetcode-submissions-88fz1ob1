class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            given:
                nums: array of integers
            return:
            all triplets
            nums[i] + nums[j] + nums[k] == 0
            the indices must be distinct

            nums = [-1,0,1,2,-1,-4]
            constraints:
                - no duplicate triplets

                - we need to sort to avoid duplicate triplets


            nums sorted --> [-4, -1, -1, 0, 1, 2]

            we need 3 pointers, we can use an anchor pointer and then two pointer for the remainder of the array
            do this with every possible anchor

            
        '''
        nums.sort()

        res = []

        for i in range(len(nums)):
            anchor = nums[i]
            if i > 0 and anchor == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            #handle duplicates here
            while l < r:
                three_sum = anchor + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    #duplicate check
                    res.append([anchor, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

        