class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            given an integer array heights, heights[i] = height of the ith bar

            you may choose any two bars to form a container
            return the max amount of water a container can store
            

            height = [1,7,2,5,4,7,3,6]
            36
            index 7 - index 1 = 6 * min of two bars 6



            area of water = height * width
            width is the difference of the two indices

            your height is capped by the lower of the two bars
            when do we move our pointers??
            - so whichever bar is smaller we move the pointer for that bar forward or back for l and r respectively



        '''
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                r -= 1
                l += 1
        return max_area



        