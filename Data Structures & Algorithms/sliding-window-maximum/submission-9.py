from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            given: array of integers nums and an integer k
            sliding window of size k that starts at the left edge of array
            window slides one position to the right until it reaches the right edge
            return a list contains the max element in each window

            nums = [1,2,1,0,4,2,6], k = 3

            first window = [1,2,1] --> 2 append to resiult
            move the window to the right
            2 again
            append 2
            move window again add 4 --> move window again
            add 4 again
            then add 6

            Monotonic Deque solution
            [1,2,3,4] --> k = 3
            values are in increasing order
            output 3
            shift window to the next position
            [2,3,4]
            max is 4 --> Brute force
            add 4 to output
            output = [3,4]

            REPEATED WORK
            - as soon as we see 1,2,3 we know 3 is grater
            so we can just eliminate 1 and 2
            even thoiugh 2 is in the window we never need to worry about the 2 again
            the older smaller elements that are STILL IN THE WINDOW AFTER SHIFTING are useless
            to eliminate values use a queue
            always decreasing order in the deque
            [1,1,1,1,1,4,5]
            since 4 is greater than the value at the top most positon of deque
            pop the top of the deque
            make the same comparison again and again and again after all the comparisons 
            we add the new value 4


            the leftmost value of the deque represents what we add to the output


            then shift the window
            is 5 > 4 (value at top of the deque)
            4 is essentially irrelevant
            so we ad 5 to the deque

            add the 5 (leftmost position) to the output
            output = [4,5]

            if the value is smaller than the top of the queue add the 7 
            DECREASING ORDER
            leftmost value would thus be the max
            once a value is not in bounds we popleft()


        '''
        res = []
        q = deque() #contains indices
        l, r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                #while smaller values exist in the queue
                q.pop()
                #removes all the smaller values
            #now add the new value to the queue
            q.append(r)

            #if left is out of bounds, remove it from the window
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                #window is at least size k
                res.append(nums[q[0]])
                #left is onlu incremented when window is size k
                l += 1
            r += 1
        return res



        
            