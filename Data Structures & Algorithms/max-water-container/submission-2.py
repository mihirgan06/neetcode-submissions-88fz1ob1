class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            Given an integer array heights, where heights[i] represents the height of the ith bar

            
            choose any two bars to form a contianer, return max amount of water a contianer can store

            [1,7,2,5,4,7,3,6]


            youre capped by the height of the shorter of the two bars

            the width is the difference btwn the two indices u use

        '''
        l, r = 0, len(heights) -1 

        
        max_area = 0
        
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l +=1
            else:
                r -= 1
        return max_area



        