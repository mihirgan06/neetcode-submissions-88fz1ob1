class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            tou are given integer array heights, heights[i] = height of the ith bar

            choose any two bars to form a container
            return amx amount of water a container can store
            you are capped by the shorter bar
            area = width * height
            width = difference in the two pointers were using
            height = the height of the shorter of two bars



        '''
        l,r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = height * width
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        