class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            deque solution:

                basically instantiate a deque



        '''


        from collections import deque
        q = deque() #index, we can take the index find the numebr
        l = r = 0
        res = []
        while r < len(nums):
            #while right is in bounds
            while q and nums[q[-1]] < nums[r]:
                #while smaller values exist in queue, pop so we pnly have big value
                q.pop()
            q.append(r)

            #if the left val is out of bounds remove
            if l > q[0]:
                q.popleft()
                #if the window is out of bounds of window we need to remove it
            if r + 1 >= k:
                #checking right side validity
                res.append(nums[q[0]])
                #left is only incremented when window is size k
                l += 1
            r += 1
        return res


            

        