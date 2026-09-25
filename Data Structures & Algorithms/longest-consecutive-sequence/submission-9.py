class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            given an array of integers nums return the length of the longest consecutive sequence of elements that can be formed
            Consecutive sequence is a sequence of elements in which each elemnet is exactly 1 greater than previous element

            nums = [2,20,4,10,3,4,5]
            4

            2, 3, 4, 5 --> 4

            nums = [0,3,2,5,4,6,1,1]

            0, 1, 2, 3, 4, 5, 6 --> 7

            1. brute force
                sort the elements
                iterate through sorted array and append to a res if the element were processing is 1 greater than the prev element
            2. why it is inefficient
                O(n log n) sorting is a log n operaiton
            3. pattern/data structure I'm using
                Ill use a set for O(1) lookup time
            4. what my variables mean

            5. why each pointer/hashmap decision is valid
                We can iterate through the array converting theentire array into a set
                Iterate through the set
                check if x - 1 is in the set if its there continue
                checkf or x +1 continuouslt
                
            6. time + space complexity
                O(n)
        '''
        set_nums = set()
        for i in range(len(nums)):
            set_nums.add(nums[i])
        

        #we added every element into a set
        max_count = 0

        for x in set_nums:
            if x -1 in set_nums:
                continue

            local_count = 1
            
            while x + 1 in set_nums:
                x += 1
                local_count += 1
            max_count = max(local_count, max_count)
        return max_count

        