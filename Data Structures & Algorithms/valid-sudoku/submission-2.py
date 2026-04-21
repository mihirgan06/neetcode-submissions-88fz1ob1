class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        """
            Given 9x9 sudoko board board
            1. Eahc row has digits 1-9 w/o duplicates
            2. Each col has digits 1-9
            Each 3x3 has 1-9

            Approach

                Loop through each row and col, so were able to check each individual square

                Set for rows to make sure no duplicates --> sets dont hold duplicates and have a O(1) access time
                - Same for cols and boxes

        """
        rows = defaultdict(set) #O(1) to add to any of these
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box = (r // 3) * 3 + (c // 3)
                
                if val == ".":
                    continue
                if val in rows[r] or val in cols[c] or val in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)
        return True
        
                
        
        