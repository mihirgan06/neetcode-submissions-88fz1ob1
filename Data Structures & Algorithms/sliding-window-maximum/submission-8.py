from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            given: array of integers nums and integer k

            sliding window of size k
            Brute force:
            [1,2,1,0,4,2,6], k = 3

            append 2
            move the window append 2 again
            append 4
            append 4
            append 6

            Optimal Use a monotonic deque
            the front of the queue stores the max at any given window
            queue stores indices
            we pop from the left when we wanna append the max
            pop from the right if its useless



        '''
        q = deque()
        res = []
        l = 0
        r = 0
        while r < len(nums):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            if q[0] <= r - k:
                #that index fell out of range
                q.popleft()
            if r >= k - 1:
                res.append(nums[q[0]])
            r += 1
        return res

            
            

        
        