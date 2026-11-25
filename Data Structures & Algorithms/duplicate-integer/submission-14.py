from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
            given array nums
            return true if any value appears more than once
            create a hashmap tracking how much each value appears
            return true if any value appears onlt 1 time
        '''
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for num, value in counts.items():
            if value > 1:
                return True
        return False
        
        