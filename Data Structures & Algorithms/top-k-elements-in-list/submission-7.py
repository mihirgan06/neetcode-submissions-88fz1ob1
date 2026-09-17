class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_sort = [[] for _ in range(len(nums)+1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            bucket_sort[cnt].append(num)

        result = []
        for i in range(len(bucket_sort)-1, 0, -1):
            for num in bucket_sort[i]:
                result.append(num)
                if len(result) == k:
                    return result