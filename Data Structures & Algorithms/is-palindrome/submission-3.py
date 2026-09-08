class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            given a string s, return true if palindrome return false


            palindrome same forward and backward

            2 pointers move towards the middle until we find theres a mismatch
        '''
        
        s = s.lower()

        s = s.replace(" ", "")
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

            
        