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

        counts_s1 = defaultdict(int)


        for i in range(len(s1)):
            counts_s1[s1[i]] += 1
        #build the counts for all of s1
        window = len(s1)
        for i in range(len(s2) - window + 1):

            have_window = Counter(s2[i: i + window])
            if have_window == counts_s1:
                return True
        return False

            

            