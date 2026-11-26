class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            Given: heights array where heights[i] = height fo the ith bar
            may choose any two bars to form a container
            calculate the max amount of water a container can store
            for the area youre capped by the height fo the smaller bar

            we wanna calculatd an area and then update a global max area variable
            whichever of the two bars is shorter we move that pointer
        '''
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            #move both pointers
            else:

                l += 1
                r -= 1
        return max_area

