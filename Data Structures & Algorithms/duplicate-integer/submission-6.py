class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        iterate throiugh array
        check if the value in the map
        if not in the map return false
        '''
        from collections import defaultdict
        my_map = defaultdict(int)
        for i, num in enumerate(nums):
            if num in my_map:
                return True
            else:
                my_map[num] += 1
        return False

        
            

        