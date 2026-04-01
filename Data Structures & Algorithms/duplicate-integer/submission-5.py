class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return true if any value appears more than once in the array

        freq = {}
        #map to count ow many times each number appears

        for i,num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            if value > 1:
                return True

        return False
        