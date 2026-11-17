class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0
        i = 0
        j = n - 1
        while i < j:
            hi = min(heights[i], heights[j])
            wi = j - i
            ans = max(hi * wi, ans)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return ans
