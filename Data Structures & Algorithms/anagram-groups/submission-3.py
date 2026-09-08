class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Given an array strs, group all anagrams together into sublists
            anagram is a string that containst he exact same characters as a string but diff order

            strs = ["act","pots","tops","cat","stop","hat"]
            output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

            Determine what makes a group of strings an anagram then group them tgt in sublists
            have an overall res array

            Iterate through each string have a diffgerent count for each string 


            Using ord to normalize it to 0 - 25
        '''
        res = []
        my_map = defaultdict(list)

        for string in strs:
            alpha = [0] * 26
            for ch in string:
                alpha[ord(ch) - ord('a')] += 1
            key = tuple(alpha)
            my_map[key].append(string)
        return list(my_map.values())
            
            
        
            
                


        