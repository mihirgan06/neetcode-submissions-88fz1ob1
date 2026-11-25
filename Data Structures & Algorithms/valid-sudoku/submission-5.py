class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            given a 9x9 sudoko board
            board is valid if:
            1. each row must contain 1-9 without duplicates
            2. each column must contain 1-9 without duplicates
            3. each of the 9 3x3 subboxes of the grid must contain the digits 1-9 without duplicates
            hold 3 sets to prevent duplicates

            1. for row
            2. for col
            3. box
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
    
                box = (r // 3) * 3 + (c // 3)
                if board[r][c] == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[box].add(board[r][c])
        return True

                
                
        
                

        
            
        