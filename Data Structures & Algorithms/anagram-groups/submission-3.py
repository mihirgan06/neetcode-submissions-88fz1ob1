class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = {}
        
        #we can keep a count for each character in the alphabet

        for i, string in enumerate(strs):
            res_list = [0] *26
            for char in string:
            #count the times
            #eat --> 1e, 1a, 1t
                index = ord(char) - ord('a')
                res_list[index] += 1
            key = tuple(res_list)
            if key in my_map:
                my_map[key].append(string)
            else:
                my_map[key] = [string]
        return list(my_map.values())





        