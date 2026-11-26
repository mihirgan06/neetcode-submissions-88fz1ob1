class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            Given: string s
            return true if palindrome else false

            palindrome is same forward and ba kward

            
            remove all the spaces and clean up the string first
            start two pointers left and right
            if s[l] != s[r] return false
            keep moving inwards if it is the same till theyre at the middle return true

        '''
        s = s.lower()
        s = s.strip()
        l, r = 0, len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True