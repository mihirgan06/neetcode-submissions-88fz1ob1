class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            1. brute force

            2. why it is inefficient
            3. pattern/data structure I'm using
                2 pointer approach
                start at left and right
                count all the water cells
                we only move left and right pointers based on heightL and heightR
                the water there is maxheight - height at the pointer

            4. what my variables mean
            5. why each pointer/hashmap decision is valid
                
            6. time + space complexity
        '''

        trapped_water = 0
        l, r = 0, len(height) - 1
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
            

        