class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
            queens can attack vertically, horizontally, or diagonal
            We need to simulate placing queens in all positions until we find a place where they arent attacking

            n = 4 (4x4 board)

            - Q - -
            - - - Q
            Q - - - 
            - - Q -

            - - Q -
            Q - - -
            - - - Q
            - Q - -

            n = 1
            Q
        '''

        res = []
        board = [['.'] * n for i in range(n)]
        #create the empty board  (n x n)
        cols = set()
        posDiag = set()
        negDiag = set()
        #use sets for these so if we place a queen there we cant in the future

        def isValid(row, col):
            if col in cols:
                return False
            if row + col in posDiag:
                return False
            if row - col in negDiag:
                return False
            return True

        def backtrack(row):
            '''start at index 0 of the board and simulate placing of queens until we find a valid working solution
            '''
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for col in range(n):
                if not isValid(row, col):
                    continue
                board[row][col] = "Q"
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                backtrack(row + 1)
                #remove

                board[row][col] = "."
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
        backtrack(0)
        return res
                
            
            

