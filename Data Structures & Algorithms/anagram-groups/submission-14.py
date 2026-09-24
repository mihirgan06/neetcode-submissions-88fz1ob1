class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            given an array of strings strs, group all anagrams together into sublists

            return output in any order

            anagram is a string where the exact chatacters but diff order
            strs = ["act","pots","tops","cat","stop","hat"]
            [["hat"],["act", "cat"],["stop", "pots", "tops"]]

            same characters, diff order
            len(string) should be equal

            


        '''

        groups = defaultdict(list)

        

        #we want to create alpha within a loop so it resets for every word
        for word in strs:
            alpha = [0] * 26
            for ch in word:
                alpha[ord(ch) - ord('a')] += 1

            key = tuple(alpha)

            groups[key].append(word)
        return list(groups.values())
    
        
        