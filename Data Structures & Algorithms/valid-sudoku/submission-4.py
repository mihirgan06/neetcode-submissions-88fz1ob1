class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            given a 9x9 board 

            1. each row must contain the digits 1-9 without duplicates
            2. each column must contain the digits 1-9 2ithout duplicates
            3. each of the nine 3x3 subboxes muyst contain digits 1-9 without duplicates

            true if valid else false


            3 sets for rows cols, and boxes
            the way we do this is we have the set as the avtual value type for the rows, cols, boxes

            rows[0] would correspond to the set for row 0.... row[9] would correspond to the set for row 9


            nested loop to traverse the board check membership for each set
            


           

        '''
        from collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)


        ROWS = len(board)
        COLS = len(board[0])

        #iterate through board and check membership
        for r in range(ROWS):
            for c in range(COLS):
                box = (r // 3) * 3 + (c // 3)
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r //3, c// 3)]:
                    return False #duplicate spotted
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        return True
                
                    





        