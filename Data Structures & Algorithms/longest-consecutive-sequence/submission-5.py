class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            given an array of integers nums

            return the legnth of consecutive sequence of elements that can be formed

            consecutive elements is 1 greater than the prev element

            O(n)

            nums = [2,20,4,10,3,4,5]

            4

            2,3,4,5



            nums = [0,3,2,5,4,6,1,1]
            output = 7



            cant sort it it would be O(nlogn)


            we only want to start sequences at the start of a sequence
            - we can check this by checking if nums[i] - 1 exists in the array, if it does not then nums[i] would be the start of a sequence
            - then we just return the longest subsequece

        '''
        
        

        longest = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while (num + length) in nums:
                    length += 1
                longest = max(longest, length)
        
        return longest