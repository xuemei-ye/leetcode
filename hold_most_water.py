class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxh = 0
        maxw = 0
        maxvalue = 0
        right = 0
        left = len(height) - 1
        while right < left:
            h = min(height[right],height[left])
            w = left - right
            if (h > maxh or w > maxw) and h * w > maxvalue:
                maxvalue = h * w
                maxh = h
                maxw = w
            if height[right] > height[left]:
                left -= 1
            else:
                right += 1
        return maxvalue