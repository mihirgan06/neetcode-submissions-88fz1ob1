class Solution:
    from collections import defaultdict
    def singleNumber(self, nums: List[int]) -> int:
        '''
            given a non-empty array of integers nums
            Each integer appears twice except once
            return tje integer that only appears once
        '''
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            if count == 1:
                return num

                    
        