# 方法一：递归，O(2^n）| 问题重复计算
#
# 方法二：不断将前两个数累加 O(n), 滚动数组，第三个数等于前两个数的和，不断往前滚动
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n

        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q
        return r