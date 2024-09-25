
import copy

# 知识点：python 矩阵复制是复制指针，导致两个变量指向同一个对象，对新矩阵的修改会影响原矩阵
# 引用拷贝与值拷贝的区别
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cm = copy.deepcopy(matrix)
        r = len(matrix)
        # c = len(matrix[0])
        for i in range(r):
            for j in range(r):
                matrix[j][r-i-1] = cm[i][j]



# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/rotate-image/solutions/526980/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new

