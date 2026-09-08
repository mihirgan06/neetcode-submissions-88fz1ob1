class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            Given an array of strings strs, group all anagrams together into sublists
            return output in any order
            anagram is a string that contains same characters as another string but the
            order can be different

            strs = ["act","pots","tops","cat","stop","hat"]

            [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        '''
        groups = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            for ch in word:
                #normalize from 0 - 25 and append for each appearance
                alpha[ord(ch) - ord('a')] += 1
                
            key = tuple(alpha)
            groups[key].append(word)
        return list(groups.values())
