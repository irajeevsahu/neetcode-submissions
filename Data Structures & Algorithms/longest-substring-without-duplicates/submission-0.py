class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in sets:
                sets.remove(s[l])
                l += 1
            sets.add(s[r])
            ans = max(r - l + 1, ans)
        return ans
