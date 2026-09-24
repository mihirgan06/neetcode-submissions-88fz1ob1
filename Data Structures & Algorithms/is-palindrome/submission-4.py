class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            given a string s return true if it is a palindrome else false


            palindrome same forward and backward
            Approach:
            - set everything to lowercase

            - start left and right pointers
            iterate towards middle

        '''
        s = s.lower()
        s = s.strip()
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        