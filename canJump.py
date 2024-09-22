class Solution:
    state_map = dict()

    def canJump(self, nums) :
        if len(nums) == 1:
            return True

        idx = 0
        idx += nums[idx]
        while idx > 0:
            if idx >= (len(nums) - 1):
                return True
            if nums[idx] == 0 and idx <= 0:
                self.state_map[idx] = False
                return False
            if idx in self.state_map.keys():
                return False
            print(nums[idx:])
            if not self.canJump(nums[idx:]):
                self.state_map[idx] = False
                idx -= 1
            else:
                return True
        return False

    # 官方思路：记录最远距离
    def canJump_better(self, nums) :
        furtherest = nums[0]
        for i in range(len(nums)):
            if furtherest < i:
                return False
            furtherest = max(furtherest, i + nums[i])
            if furtherest >= len(nums) -1:
                return True
        return False




s = Solution()
l = s.canJump([1,2,3])
print("l", l)



