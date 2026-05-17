class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ''''
            given m x n 2D integer matrix and a target
            Each row in matrix is non-dec (inc) order!

            First integer is greater than the last integer of the prev row
            We just return T/F based on whether the value is in the matrix

            we can entirely disregard a row since its in inc order
            

            Approach:
                SLightly altered 2D binary search alg.
                Can we actually disregard an entire row?
                First binary search to find the correct row, and then binary search within the row to find the specific value

        '''
        row = len(matrix)

        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom ) // 2 #integer division
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                #we found the right row
                break
        l, r = 0, len(matrix[0]) - 1
        #binary search the row we chose
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


            

                
        