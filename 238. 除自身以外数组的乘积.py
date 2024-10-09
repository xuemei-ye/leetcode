from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        map = {}
        for num in nums:
            if num not in map.keys():
                ml = nums.copy()
                ml.remove(num)
                res = reduce(lambda x, y: x * y, ml)
                answer.append(res)
                map[num] = res
            else:
                answer.append(map[num])
        return answer


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        l, r, answer = [0] * length, [0] * length, [0] * length,

        l[0] = 1
        for i in range(1, length):
            l[i] = l[i - 1] * nums[i - 1]

        r[length - 1] = 1
        for i in reversed(range(length - 1)):
            r[i] = r[i + 1] * nums[i + 1]

        for i in range(length):
            answer[i] = l[i] * r[i]

        return answer
