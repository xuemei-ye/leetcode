# 128 最长连续序列
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

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        nums.sort()
        print(nums)
        count = 1
        max_count = 1
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                count += 1
                max_count = max(max_count, count)
            elif nums[i+1] == nums[i]:
                continue
            else:
                count = 1
        return max_count


class Solution_Better(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current = 1
                while current_num + 1 in nums:
                    current += 1
                    current_num += 1
                max_count = max(max_count, current)

        return max_count

# 思路：遍历list，如果前一个数不在list中，则开始遍历，否则跳过。—— 从最长序列的最小值开始遍历，跳过中间的值
