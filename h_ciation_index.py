class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cs = sorted(citations)
        h = 0
        for i in range(len(cs)):
            if cs[i] <= (len(cs) - i):
                h = max(h, cs[i])
            else:
                break

        while True:
            h += 1
            count = len([x for x in cs if x >= h])
            if h <= count and h <= len(cs):
                continue
            else:
                h -= 1
                break

        return h

# 用二分查找更快