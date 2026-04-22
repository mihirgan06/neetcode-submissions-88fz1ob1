class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            Return true i fpalindrome else false

            same forward or backward
            easy 2 pointer
            pointer at right and pointer at left
            check if the char is =

        '''

        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            # if right is not alphanumeric → skip
            if not s[r].isalnum():
                r -= 1
                continue

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

                
        