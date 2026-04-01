class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary Search Algorithm: we want to treat the entire 2D grid as a singular 1D sorted array and perform a single binary search

        #We want to Flatten the Matrix, so it would have rows * cols elements
        rows = len(matrix)
        cols = len(matrix[0]) if matrix else 0
        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            row = mid //cols
            col = mid % cols
            

            if target < matrix[row][col]:
                high = mid - 1
            elif target > matrix[row][col]:
                low = mid + 1
            else:
                return True

        return False