class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
            given an array of strings strs, group all anagrams together into sublists
            return output in any order
            anagram is a string that contains exact same characters as another string

            ordering can be different
            approach brute force
            * sort all the strings and hten compare the counts and check if length is same


            hold an alphabet array which has the coutns for each string

            like for act

            alpha would look like this
            [1,0,1.....1 for t...]

            we can have a hashnmap that maps the same akphabet to a list of all words satisfyung that alphabet counts





        '''
        counts = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            for ch in word:
                #use ord in order to conver the letters into array indices
                alpha[ord(ch) - ord('a')] += 1
            counts[tuple(alpha)].append(word)
        return list(counts.values())
            
        
        
        
        

        