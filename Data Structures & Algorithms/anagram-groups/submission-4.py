class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            for ch in word:
                alpha[ord(ch) - ord('a')] += 1
            key = tuple(alpha)
            groups[key].append(word)
        return list(groups.values())
            
                
        