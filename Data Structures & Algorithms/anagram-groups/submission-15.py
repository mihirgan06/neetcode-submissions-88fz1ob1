class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            1. brute force
                We could sort each word in strings
                then append to a hashmap having the keys be the sorted strings
                the values could be all the strings whihc are anagrams of the sorted version
                return a list version of this hashmap values

            2. why it is inefficient
                THis would be O(nlogn) since we are sorting
            3. pattern/data structure I'm using
                we could create a hashmap with list as the values
                the values are the anagrams itself
                the key would be the alphabet as an array of 26 spots corresponding to counts for each letter of the alphabet

            4. what my variables mean
                hashmap of list
                iterate through strings
                create an alphabet array
                increment coutns for the alphabet
                for every word there is a signature, and we are creating a list of words with that signature
            5. why each pointer/hashmap decision is valid
                
            6. time + space complexity
                This would be O(n *m)
                n words, m characters per word
                each lookup is O(1) or O(26) which is a constant so O(1) amortized
        '''
        groups = defaultdict(list)

        for word in strs:
            alpha = [0] * 26
            for ch in word:
                alpha[ord(ch) - ord('a')] += 1
        
            groups[tuple(alpha)].append(word)
        return list(groups.values())

        
        