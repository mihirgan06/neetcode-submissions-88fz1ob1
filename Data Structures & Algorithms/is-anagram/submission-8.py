class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        hashmap = dict()
        hashmap2 = dict()
        for i in range(len(s)):
            schar = s[i]
            tchar = t[i]
            if schar in hashmap:
                hashmap[schar] += 1
            else:
                hashmap[schar] = 0
            if tchar in hashmap2:
                hashmap2[tchar] += 1
            else:
                hashmap2[tchar] = 0
        for i in range(len(s)):
            schar = s[i]
            if(schar not in hashmap2 or hashmap[schar] != hashmap2[schar]):
                return False
        return True
            