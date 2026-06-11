class Solution:
    from collections import deque
    def solve(self, board: List[List[str]]) -> None:
        '''
            If a region of 0s is surrounded by Xs then its surrounded and you convert them into Xs
            Push every 0 into a queue, only bfs in 4 dirs fromn the 0s and if theres a biundary then dont change it
        '''
        ROWS, COLS = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == 'O' and (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1):
                        q.append((r,c))
                        board[r][c] = "T"
            
            #push every coordinate thats a 0 into the queue

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                        continue
                    if board[nr][nc] != 'O':
                        continue
                    board[nr][nc] = 'T'
                    q.append((nr, nc))
        bfs()
            #FLip surrounded 0s

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"