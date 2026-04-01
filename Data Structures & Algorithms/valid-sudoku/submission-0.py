class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        We need to scan over the rows for duplicates
        Scan over cols for duplicates
        Scan over 3x3 squares for duplicates --> Set
        Aimed Time complexity = O(N^2)
        '''
        #set is perfect because membership check = O(1)
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r //3, c //3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True
                
                
                




