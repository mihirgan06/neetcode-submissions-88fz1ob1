class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''Given an integer array heights
        heights[i] represents height of ith bar

        Choose two batrs to form container



        Approach:
                The amt of water is directly influenced by the area

                Height of bars and width
                We need to maximize the distance between the bars and pick the tallest bar and ig second tallest
                Water is capped off by the height of the shorter of the two bars that we choose


        '''

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            width = r - l
            #dont put inside the boolean cuz we wanna compute the area irregardless
            area = min(heights[l], heights[r]) * width
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_area
            



        