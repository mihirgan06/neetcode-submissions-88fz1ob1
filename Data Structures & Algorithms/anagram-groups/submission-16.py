from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            given an array of strings strs, group all anagrams together into sublists you may return the output in any order
            strs = ["act","pots","tops","cat","stop","hat"]
            [["hat"],["act", "cat"],["stop", "pots", "tops"]]

            we can use an alphabet array of size 26

            convert all the letters to a count using ord
            use the alphabet as the key for our hashmap by making it a tuple so its immutable
            have a seperate alphabet count and use the alphabet count for the word as the key


        '''

        groups = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            #for every word have its own alphabet count


            for ch in word:
                alpha[ord(ch) - ord('a')] += 1
            groups[tuple(alpha)].append(word)
        return list(groups.values())
        
        