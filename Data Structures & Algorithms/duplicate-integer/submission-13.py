class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            given an integer array nums return true if any value appears more than once in the array return false
            Add every elem to a hashmap if the count for the element is > 1 return true else false
        '''
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
        for num, count in counts.items():
            if count > 1:
                return True
        return False