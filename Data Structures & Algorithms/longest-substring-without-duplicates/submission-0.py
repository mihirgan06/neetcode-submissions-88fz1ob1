class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #given string s, find the length of the longest substring WITHOUT duplicate characters

        #substring is a contiguous sequence of characters within a string

        #looking for O(N) time

        #Brute Force:
            #we can do a two pass through, and keep adding to a counter
        

        #efficient: we can add to a hashmap, keepig track of how many times each character appears
        #keep iterating till we find the count of one letter > 1, then escape the loop and return
        #the above solution does NOT work for all strings, as it will fidn the first substring, but will entirely ignore a longer one later in the stiring

        #Thus we must use sliding window

        char_set = set() #use the set in order to hold the chars CURRENTLY IN WINDOW

        #for sliding window we need two pointers
        
        left = 0 #left index of the window
        res = 0 #the best result yet
        
        for right in range(len(s)):
            #right index of window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])

            res = max(res, right - left + 1)
        return res
            