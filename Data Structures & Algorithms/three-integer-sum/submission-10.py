class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            given an array nums
            return all the triplets [nums[i], nums[j], nums[k]]

            where nums[i] + nums[j] + nums[k] == 0
            i, j, k are distinct

            No duplicates


            nums = [-1,0,1,2,-1,-4]
            [[-1,-1,2],[-1,0,1]]
            nums = [0,1,1]

            []

            Sort the array
            [-1,0,1,2,-1,-4]
            turns into

            [-4, -1, -1, 0, 1, 2]


            start an anchor at 0
            then start two pointers from anchor + 1 and end of array
            try all possible with that anchor
            append all possible triplets with that anchor then move anchor move forward


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
                if anchor + nums[l] + nums[r] < 0:
                    l += 1
                elif anchor + nums[l] + nums[r] > 0:
                    r -= 1
                
                #move pointers again becasue we keep searching
                else:
                    res.append([anchor, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
                
                

        

        