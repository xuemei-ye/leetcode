import numpy as np
class Solution:
    def add_boarder(self, board: List[List[int]]) -> List[List[int]]:
        board = np.array(board)
        new_board = np.pad(board, pad_width=1, mode='constant', constant_values=0)
        return new_board

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = self.add_boarder(board)
        # res = np.zeros((len(board), len(board[0])))
        for i in range(1, len(new_board) - 1):
            for j in range(1, len(new_board[0]) - 1):
                value = (new_board[i - 1][j - 1] + new_board[i][j - 1] + new_board[i - 1][j] +
                         new_board[i - 1][j + 1] + new_board[i][j + 1] + new_board[i + 1][j] +
                         new_board[i + 1][j - 1] + new_board[i + 1][j + 1])

                if new_board[i][j] == 1:  # 活细胞
                    if value < 2 or value > 3:
                        board[i - 1][j - 1] = 0  # 活细胞死亡
                    else:
                        board[i - 1][j - 1] = 1  # 活细胞存活
                else:  # 死细胞
                    if value == 3:
                        board[i - 1][j - 1] = 1  # 死细胞复活

        return board

    def gameOfLife_InPlace(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (1, -1), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):

                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    if (r >= 0 and r < rows) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1

                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0

# 示例使用
# board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
board = [1,1],[1,0]
sol = Solution()
result = sol.gameOfLife(board)
print(result)