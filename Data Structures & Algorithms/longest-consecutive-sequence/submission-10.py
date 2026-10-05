class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            given an array of integers nums, return the length of the longest consecutive sequence of elemnts where each element is exactly 1 > than previous element


            ELEMENTS DO NOT HAVE TO BE CONSECUTIVE IN ORIGINAL ARRAY
            nums = [2,20,4,10,3,4,5]

            we obv cannot sort that would be O(nlogn) but if we were to it would be super simple we would just keep iterating as nums[i] + 1 is in the array keep appending

            rather in o(n) we can convert nums to a set

            then iterate through the set if x - 1 is in the set we can search for x
            nums = [2,20,4,10,3,4,5]

            say were processing 2 were looking next for 3 which can be done in O(1) 
            then we look for 4 --> O(1)
            then 5 --> O(1)
            then 6 not in the array this count ends

            thne we try for 20
            no 21 
            best count so far is 6
            then try for 4 --> 5 


        '''

        set_nums = set(nums)
        #convert nums into a set
        best_count = 0

        for x in set_nums:
            if x - 1 in set_nums:
                continue
            count = 1
            while (x+1) in set_nums:
                x += 1
                count += 1
            best_count = max(count, best_count)
        return best_count


        