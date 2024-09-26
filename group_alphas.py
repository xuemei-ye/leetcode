# collections.defaultdict 是 Python 中的一个字典子类，允许你指定一个默认值的类型，
# 当你访问一个不存在的键时，它会自动为该键创建一个新值，而不抛出 KeyError。
# 使用 defaultdict(list) 可以让你创建一个字典，其中每个键的默认值是一个空列表。

# 找到不变的key，往里填字符串，而不需要去统计出现的次数，观察不变之处。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())