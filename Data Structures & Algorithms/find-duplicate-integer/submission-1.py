class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            I mean obv brute force is just that you have a hashmap and count each occurance return the integer that appears > 2 times


            But obv this requires a linked list:
                Convert

            USE Slow and fast pointers
            REVISIT THIS PROBLEM THIS IS SO NOT INTUITIVE
        '''
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow