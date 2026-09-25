class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            given an integer array nums and an integer k,
            return the k most frequent elements within the array
            1. brute force
                You could use a heap --> O(nlogn)
                heapify the elements in the array and just heappop the k largest elements as a max heap and append to an array
            2. why it is inefficient
                O(nlog n)
            3. pattern/data structure I'm using
                I could use bucket sort

                the most an element could show up is len(nums) time
                so if i create a bucket sort, where the buckets correspond to frequency
                bucket_sort[1] would have all the elements showing up 1 time

                where bucketsort[n] wehre n is the full sie of the array would have all the elements if any that show up n times

                We could start from the end of the array and append to res until len(res) == k
            4. what my variables mean
                bucketsort refers to a bucket array where each bucket corresponds to a frequency
            5. why each pointer/hashmap decision is valid
            6. time + space complexity
                O(n) 
        '''
        counts = defaultdict(int)
        bucket_sort = [[] for i in range(len(nums) + 1)]
        #start by getting the hashmap of frequencies for each element
        for i in range(len(nums)):
            counts[nums[i]] += 1
        #iterate through the k, v of the hashmap and append the corresponding num for each count
        for num, count in counts.items():
            bucket_sort[count].append(num)
        res = []
        for i in range(len(bucket_sort) - 1, -1, -1):
            for num in bucket_sort[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        
        
        