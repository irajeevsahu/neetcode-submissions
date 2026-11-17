class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n
        maxi = height[0]
        ans = 0
        for i in range(n):
            if maxi < height[i]:
                maxi = height[i]
            prefix[i] = maxi
        maxi = height[n - 1]
        for i in range(n - 1, -1, -1):
            if maxi < height[i]:
                maxi = height[i]
            suffix[i] = maxi
        for i in range(n):
            ans += min(prefix[i], suffix[i]) - height[i]
        return ans
