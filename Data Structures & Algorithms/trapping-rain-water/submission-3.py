class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            given an array of non-negative integers height
            each value height[i] = height of bar shich has a width of 1
            return the total amount of water that can be trapped between the bars
            water can fill the gaps between bars
            so we need to calculate multiple subareas and compute the total


            height = [0,2,0,3,1,0,1,3,2,1]

            l starts at 0, r starts at 9
            total area here is (9 - 0) * 1

            if one bar > than the other we can move the smaller pointer
            but keep computing area at each slot


            


        '''
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        max_water = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                max_water += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                max_water += rightMax - height[r]
        return max_water
            

        