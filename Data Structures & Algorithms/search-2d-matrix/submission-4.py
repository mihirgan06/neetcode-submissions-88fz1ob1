class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
            given an m x n 2d integer array matrix and integer target
            each row in matrix is sorted in non-dec order

            first integer of every row is greater than the last intgegr of the prev row

            true if target exists else false
            matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

            we can flatten the 2d matrix into a single array in O(n)
            then perform binary search on the single array

        '''

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1


        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1

            else:
                l = mid + 1
        return False
