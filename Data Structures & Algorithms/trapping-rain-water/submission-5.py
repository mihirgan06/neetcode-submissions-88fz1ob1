class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            given:
                array of non-negative integers height, represents an elevation map

                each value, height[i] --> height of a bar
                with a width of 1

            return:
            - total amoutn of water that can be trapped between the bars

            the amount of water that can be trapped at any given height is the min of the bars to left and right - height at that pointer

        '''

        l, r = 0, len(height) - 1
        trapped_water = 0
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                trapped_water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trapped_water += maxR - height[r]
        return trapped_water
            


        