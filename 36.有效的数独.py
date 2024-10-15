class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j]) - 1
                bl = (i // 3) * 3 + (j // 3)
                if row[i][num] or col[j][num] or block[bl][num]:
                    return False
                row[i][num] = col[j][num] = block[bl][num] = 1

        return True 