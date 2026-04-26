class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
            ok the largest rectangle is capped by two things
            the min of a stretch of bars
            but each box has a width of 1, so we can add that shit up
            but the major cap is the min of the bars


            for ex 1:
                [7,2,2,4] the min height of the bars is 2, the wicdth is 4, cuz we can stretch that for 4 blocks 


            for ex 2:
                [1,3,7] to amximize arrow we can take 7 as the max height
                and then we have 1 as width
            EXTEND WIDTH OF RECTANGLE AS LONG AS ALL BARS IN THE STRETCH >= HEIGHT
            

            o(N) time -- intended
        '''

        stack = [] #pair: (index, height)
        maxArea = 0
        width = 1

        for i, height in enumerate(heights):
            start = i #start at the beginning
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                maxArea = max(maxArea, h * (i - index)) #i - index = width
                start = index
            stack.append((start, height))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
            
            


