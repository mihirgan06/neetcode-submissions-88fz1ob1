class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Given: array of non-negative integers height which represent an elevation map
        height[i] = height of a bar
        width of 1 for each bar
        return the total amount of water that can be trapped between the bars


        in order to trap water there must be bars to the left and right
        water can be trapped above the bar

        height = [0,2,0,3,1,0,1,3,2,1]
        l = 0
        r = 9

        have a max L and max R
        maxL = 0 maxR = 1
        maxL < maxR 
        so move l to the right
        
        
        


        '''
        max_water = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]


        while l < r:
            if maxL < maxR:
                l += 1
                

                maxL = max(maxL, height[l])
                max_water += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                max_water += maxR - height[r]
        return max_water




        