class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #initialize two pointers at firtst index and last

        nums.sort()
        #needed for 2 pointers
        result = []

        
        

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            third = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                int_sum = third + nums[left] + nums[right]
                if int_sum < 0:
                    left += 1
                if int_sum > 0:
                    right -= 1
                if int_sum == 0:
                    result.append([nums[left], nums[right], third])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


        