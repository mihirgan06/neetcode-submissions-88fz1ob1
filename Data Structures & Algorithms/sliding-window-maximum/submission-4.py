class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            given ana rray of integers nums and an integer k
            there is a sliding window of size k starting at left edge
            wineo wslides one poisiton to right until reaches right edge
            Deque:
            [1,2,3,4], k = 3
            3 is the first max
            output: 3
            shift window
            4 is the next m ax
            output: 3,4
            deque: always decreasing
            keep popping till the new value is the max of our window

        add the leftmost value to our res then shift



        adding and popping to a deque is O(1) doing this n times is O(n)


        [8,7,6,9], k = 2

        window 1 = [8,7]
        add 8 to the queue, 7 < 8
        add 7 to our queue 
        queue is in decreasing order 8 and then 7
        so dont pop and append 8 to the res

        window2  [7,6]
        8 no longer in our window so we pop the 8 popleft
        add the 6 to our window 
        max is 7 add to output
        last window is [6,9]
        pop 7 from the leftmost position
        9 > 6
        pop from the right
        add 9 to our res

        '''

        
        res = []
        q = deque() #can contain indices
        l, r = 0, 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            #remove left val from window
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res




            
        