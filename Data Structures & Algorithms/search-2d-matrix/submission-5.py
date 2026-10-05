class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
            Given:
            - m x n 2D integer array matrix and an integer target

            - each row in matrix is sorted --> CLEAR GIVEAWAY FOR BINARY SEARCH
            - first interger of every row is greater than the last integer of the prev row

            return:
            - true if target exts within matrix or false otherwise
            matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10


            Flatten mentally


            1,3,5,6,10,11,16,20,23,30,34,60

            rows * cols - 1 = 11 which is the last index of this virtiually flattened array
            mid = 6





        '''
        rows, cols = len(matrix), len(matrix[0])
        # 3 and 4 respectively for first ex
        l, r = 0, rows * cols - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                l = mid + 1
            else:
                r = mid - 1
        return False




        