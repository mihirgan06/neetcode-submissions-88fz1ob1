from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
            given:
            integer array nums and integer k
            --> k most frequent elemnets within the array
            nums = [1,2,2,3,3,3], k = 2

            the most any element can show up is len(nums) times

            bucket sort approach
            bucket_sort = [nums appearing 0 times, nums appearing 1 times, nums appearing 2.....]
            iterate from the right till we have k elements in our res array
        '''




        bucket_sort = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)

        for i in range(len(nums)):
            counts[nums[i]] += 1
        
        #we now have counts for each element
        #iterate through the k, v of the hashmap and append the corresponding num for each count
        for num, count in counts.items():
            bucket_sort[count].append(num)
        

        res = []
        for i in range(len(bucket_sort) - 1, -1, -1 ):
            for num in bucket_sort[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        


        