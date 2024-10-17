
class Solution:

    def dfs(self, grid :List[List[str]], row, col) -> list[list[str]]:
        grid[row][col] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(row -1 ,col), (row +1, col), (row, col -1), (row, col +1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                self.dfs(grid, x, y)


    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt


