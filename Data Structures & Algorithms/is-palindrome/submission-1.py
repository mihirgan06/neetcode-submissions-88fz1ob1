class Solution:
    def isPalindrome(self, s: str) -> bool:
        #palindrome reads the same both forward and backwards
        #we need to als strip of all non-alphanumeric chars

        #two pointers, one at left of string, one at right

        #we iterate the two pointers towards each othr, comparing their equality
        #if left ever does NOT equal right retunr false

        cleaned = " ".join(c.lower() for c in s if c.isalnum())


        left = 0
        right = len(cleaned) - 1
        

        while left <= right:
            if cleaned[left] == cleaned[right]:
                left += 1
                right -= 1
            elif cleaned[left] != cleaned[right]:
                return False
        
        return True
            



        