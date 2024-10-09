# 给定一个未排序的整数数组
# nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为
# O(n)
# 的算法解决此问题。
#
#
#
# 示例
# 1：
#
# 输入：nums = [100, 4, 200, 1, 3, 2]
# 输出：4
# 解释：最长数字连续序列是[1, 2, 3, 4]。它的长度为
# 4。
# 示例
# 2：
#
# 输入：nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# 输出：9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums == None:
            return 0
        nums.sort()
        ml = 1
        l = 1
        for i in range(len(nums)-1):
            if  nums[i] == nums[i+1] :
                continue
            if nums[i] == nums[i+1] - 1:
                # print(l)
                l += 1
            else:
                l = 1
            ml = max(l, ml)
        return ml


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums == None:
            return 0
        nset = set(nums)
        maxl = 0

        for num in nset:
            cn = num
            if cn - 1 not in nset:
                curl = 0
                while cn in nset:
                    curl += 1
                    cn += 1
                maxl = max(maxl, curl)

        return maxl


