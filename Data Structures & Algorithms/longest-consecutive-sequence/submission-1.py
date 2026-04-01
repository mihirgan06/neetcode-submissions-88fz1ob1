class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #O(N) so we shouldnt use default sort

        #we can make a hashmap and add to the map iff the element is strictly 1 greater than the previous element, return the length of the map

        #ok but how do we add the original value to the map is what im thinking

        #in the sense of like we need to add an original value tp compare to, but that might not be apart of the sequence at all

        #WE CHECK FOR A LEFT NEIGHBOR

        my_set = set(nums)
        #now we have a set

        longest_seen = 0
        for num in my_set:
            if (num - 1) not in my_set:
                length = 1
                #start of a streak
                while (num + length) in my_set:
                    length += 1
                longest_seen = max(length, longest_seen)
        return longest_seen


        
        