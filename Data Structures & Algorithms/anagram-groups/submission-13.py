class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorted() = o(log n)
        #sorted()==sorted() -> o(n * log n)
        #sort the original list of anagrams, so length of the strings 
        #are grouped
        #then anagram compare only the same length strings tgther
        #if they are not anagram, put as a seperate hashmap entry
        #at the end, return the list
        # if not strs:
        #     return []
        # hashmap = {}
        # hashmap[(strs[0],)] = 0
        # for i in range(1, len(strs)):
        #     found = False
        #     t = strs[i]
        #     for k,v in list(hashmap.items()):
        #         if len(k[0]) == len(t) and sorted(k[0]) == sorted(t):
        #             new_key = k + (t,)
        #             hashmap[new_key] = 0
        #             hashmap.pop(k, None)
        #             found = True
        #             break
        #     if not found:
        #         hashmap[(t,)] = 0
        # return [list(key) for key in hashmap]

        hashmap = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        return list(hashmap.values())