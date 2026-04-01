class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        water fills the gaps where the height is 0

        water is trapped by the bars to the right and left
        
        height of the lower of the two bars is the max height the water can go up to

        i.e. if the left bar is 2 units high, and the right is 3 units, water will fill up to 2 units

        '''

        '''
        Approach with 2 Pointers

        Start left pointer at the first index of the array, right at the last index of the array

        Keep a constant measure of the max bar seen so far on both
        Similar to max contianment of water, move the pointer where the border is smaller

        the water NEEDS two sides
        As we can see the first 0 doesnt contain any water because that is considered empty space not two sides

        OH SHIT
        When we reach a shorter boundary we know that dictates the max water that can be contained
        '''

        if not height:
            return 0

        l = 0
        r = len(height) - 1
        best_left_bar = height[l]
        best_right_bar = height[r]
        total_water = 0

        while l < r:
            if best_left_bar < best_right_bar:
                l += 1
                best_left_bar = max(best_left_bar, height[l])
                total_water += best_left_bar - height[l]
                
            
            else:
                r -= 1
                best_right_bar = max(best_right_bar, height[r])
                total_water += best_right_bar - height[r]
        return total_water
            

        