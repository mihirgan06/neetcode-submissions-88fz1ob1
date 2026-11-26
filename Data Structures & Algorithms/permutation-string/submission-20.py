class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
            Permutation in String
            Given: 2 strings s1 and s2
            return true if s2 contains a permutation of s1 or false otherwise
            true --> s2 contains a valid permutation of s1
            s1 = "abc", s2 = "lecabee"

            s1: a --> 1, b --> 1, c --> 1
            move through s2 with a window of size len(s1)
            check if the counts match within that window if not then move the entire window to the irght
            once we get a match return true
            if we go through the entire string without a permutation return false


        '''

        need = Counter(s1)
        have = Counter(s2[:len(s1)])
        if need == have:
            return True


        l = 0
        for r in range(len(s1), len(s2)):
            have[s2[r]] += 1
            have[s2[l]] -= 1
            if have[s2[l]] == 0:
                del have[s2[l]]
            l += 1
            if have == need:
                return True
        return False
