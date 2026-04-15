class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Given array of strs
        group anagrams into sublists and return
        '''
        from collections import defaultdict

        groups = defaultdict(list)
        res = []

        for word in strs:
            count = [0] * 26
            #crerate count array for 26 letters
            for c in word:
                #find the index in counts by subtracting ord('a')
                index = ord(c) - ord('a')
                count[index] += 1
            key = tuple(count) 
            #we have to pass in a tuple bc its immutable
            groups[key].append(word)
        return list(groups.values())
            
            
            
            
            
        
        