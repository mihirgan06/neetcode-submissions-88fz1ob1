class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            key = (nums[i],)
            if key not in hashmap:
                hashmap[key] = 0
            else:
                hashmap[key] += 1
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return list(item[0][0] for item in sorted_items[:k])
        