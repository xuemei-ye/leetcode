class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        target_map = dict()
        ori_map = dict()
        for r in magazine:
            if r not in target_map.keys():
                target_map[r] = 1
            else:
                target_map[r] += 1
        for r in ransomNote:
            if r not in target_map.keys() or target_map[r] <= 0:
                return False
            else:
                target_map[r] -= 1
        return True


# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/ransom-note/solutions/1135839/shu-jin-xin-by-leetcode-solution-ji8a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)