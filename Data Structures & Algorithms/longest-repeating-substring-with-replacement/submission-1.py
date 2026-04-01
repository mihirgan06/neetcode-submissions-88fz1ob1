class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #given a string s containing only ippercase english chars and an integer k
        #you can choose up to k characters of the string and replace thm with any other uppercase english cahracter

        #Looking for O(N) compelxity

        #do one pass through, add every character to a map
        #while the length of the map is less than the key k, we can swap with a character of our choosing
        
        #if the most frequent char in the window  appears maxFreq times
        #then the number of characters you'd need to replace to make the whole window that character is replacements = windowSize - maxFreq
        #window is valid if (right 0 left + 1) - maxFreq <= k
        #keep a sliding window s[left:right] --> you cna turn the entire window into one repeated letter using at most k replacement
        freq = {} #counts the occurences of each character
        res = 0 #longest substring
        left = 0 #left boundary of window
        #right is the right boundary as you iterate
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0) #this is what actually counts the values
            while(right - left + 1) - max(freq.values()) > k:
            #while the current window size - highest frequency of characters is greater than k
                freq[s[left]] -= 1
                #decreement the count
                #move left forward shrinking the window
                left += 1

            res = max(res, right - left + 1) #update the result with max bwtween the reuslt and the size of the window
            
        return res


