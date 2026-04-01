class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #given 9x9 sudoko board 
        #each row must contain digits 1-9
        #col = 1-9
        #each 3x3 must have the digits 1-9

        
        '''
            We can iterate through the rows
            Iterate through cols
            Iterate through the box
            Set for each
            add to each set
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in (range(9)):
            for c in (range(9)):
                val = board[r][c]
                box = (r // 3) * 3 + (c // 3)
                if val == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True

                
