class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            given an array of strings strs, group all anagrams into sublists
            Return in any order

            When is a str an anagram
            1. Sam characters
            2. Different order
            3. same length

            APPROACH:
                We can try to do the valid anagram check
                if the anagram is valid while iterating list, we can append to array
                Return the result array
                THis would be inefficient as we would need two loops for the words as well as the chats

            More efficient approach:
            Go thru each word sort the entire array
            Have a hashmaop with each word going to the list of strs that are anagrams for it
            append into group
            return values from map

            
        '''

        from collections import defaultdict
        groups = defaultdict(list)
        res = []
        for i, word in enumerate(strs):
            key = ''.join(sorted(word))
            groups[key].append(word)
        res.append(groups.values())
        
        return list(groups.values())
            
        