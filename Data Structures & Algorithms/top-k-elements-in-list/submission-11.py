class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            Given: ithe number of timesnteger array nums and an integer k, return the k most frequent elements within the array

            nums = [1,2,2,3,3,3], k = 2
            bucket sort
            hold an array of size nums
            the most an element can show up is NUMS times
            each slot of the array is the element that shows up that many times

            Hold a hashmap with the counts of each element

        '''

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        bucket_sort = [[] for i in range(len(nums) + 1)]

        '''
        [7,7]
        7 --> 2
        nums = [1,2,2,3,3,3], k = 2

        1 --> 1
        2 --> 2
        3 --> 3

        build counting sort so that

        [1, 2, 3]
        return 3 and 2


        '''


        for num, count in counts.items():
            #append num rather than just equating it because multiple numbers can appear ocunts times
            bucket_sort[count].append(num)

        res = []
        for i in range(len(bucket_sort) - 1, -1, -1):
            for num in bucket_sort[i]:
                res.append(num)
            if len(res) == k:
                return res
            
        
        


        