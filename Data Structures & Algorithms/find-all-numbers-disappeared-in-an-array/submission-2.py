class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        my_set = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in my_set:
                res.append(i)
        return res