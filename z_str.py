import math

# 运动的轨迹与位置索引的对应
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        r = numRows
        t = math.ceil(len(s) / (2 * (r - 1)))
        c = t * (r - 1)
        arr = [[0 for _ in range(c)] for _ in range(r)]
        arr_r, arr_c = 0, 0
        for i in range(len(s)):
            arr[arr_r][arr_c] = s[i]
            if i % (2 * (r - 1)) < r - 1:
                arr_r += 1
            else:
                arr_r -= 1
                arr_c += 1

        res = ""
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] != 0:
                    res += arr[i][j]
        return res



