class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Given an array nums, and integer k, return the k most frequent elements in array



        [2,2,2,3,3,3] k = 2
        [2,3] --> 2 most frequent elements

        [7,7] k = 1
        return 7
        Intution:

        have a count of each number from the array stored in a hashmap
        reutrn an array of the k most frequent elements from the map

        '''

        from collections import defaultdict
        


        counts = defaultdict(int)
        for i, num in enumerate(nums):
            #counts the values for each number in nums
            counts[num] += 1
        #atp we have counts for each number in the array saved in a map
        #we have a map with each # mapped to a count, and need to return the k MOST FREQUENT elements

        #the most the count for a num can be is the LENGTH of the array, if legit every element IS that number right
        #using bucket sort, we can actually group #s by their frequency
        #create a bucket for each frequency

        #create buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
            #append the value to the frequency of bucklets
        #top k
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        

        