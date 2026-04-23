class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            given heights represent an eleveation map

            Width = 1
            compute the area between every single bar bascially, 
            Area isnt just a square, it can be a complex shape
            we sium the area, so were just looking for any empty space between bars
            If the height at one pointer is less than the height of another bar, then water fills the gap

            the area here is the summation of water at each index
            If no water then nothing gets added to the area
            Sometimes its impossible to fit water if it woild overflow
            YOu need to check if theres either a talller bar next to it or if theres a boundary


            The water that can fit is the min of right and left bar and then we subtract the height at the current index

            O(N) time comp
            Edge Cases:
                1. the first bar if theres empty space left side of it then no water fits
                2. amount of water is capped by lower bar


        '''
        l, r = 0, len(height) - 1
        total_area = 0
        left_max = 0
        right_max = 0

        while l < r:
            #edge case empty left of first bar
            #need to figure out how to handle this in a semi-generic way
            #the problem is i cant just handle it w l - 1, cuz l will move each iteration
            if height[l] <= height[r]:
                #processing left        
                left_max = max(left_max, height[l])
                water_level = max(0, left_max - height[l])
                total_area += water_level
                l += 1
            elif height[r] < height[l]:   
                right_max = max(right_max, height[r])
                water_level = max(0, right_max - height[r])
                total_area += water_level
                r -= 1
            

        return total_area
            
            
                