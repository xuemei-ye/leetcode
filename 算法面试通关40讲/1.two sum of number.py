class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            x = nums[i]
            y = target - nums[i]
            if y in d.keys():
                if i != d[y]:
                    return i, d[y]

    # 固定一个数，寻找另一个数，使用 dict 来存储 O(n)
    def twoSum1(arr, target):
        hash_map = dict()
        for i, x in enumerate(arr):
            if target - x in hash_map:
                return i, hash_map[target - x]
            hash_map[x] = i