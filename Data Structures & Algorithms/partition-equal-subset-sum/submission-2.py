class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
            partition equal subset sum
            given an array of positive integers nums
            return true if you can parition the array into two subsets
            subset 1 and subset2, where sum(subset1) == sum(subset2)


            nums = [1,2,3,4]

            True
            [1,4] == [2,3]

            nums = [1,2,3,4,5]


            make each half equal to half the sum
        '''
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2


        for i in range(len(nums) - 1, -1 , -1):
            nextDP = set()

            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            #nextDP making it a new set adding all values from dp and adding all the new values
            dp = nextDP
        return True if target in dp else False




        