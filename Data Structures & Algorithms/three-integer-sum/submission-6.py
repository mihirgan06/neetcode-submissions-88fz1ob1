class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a+b+c = 0
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        result = []
        seen = set()
        for i, a in enumerate(nums):
            j = i + 1
            while j < len(nums):
                b = nums[j]
                c = -(a+b)
                if c in hashmap and hashmap[c] != i and hashmap[c] != j:
                    triplet = tuple(sorted([a,b,c]))
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append([a,b,c])
                j+=1
        return result
            