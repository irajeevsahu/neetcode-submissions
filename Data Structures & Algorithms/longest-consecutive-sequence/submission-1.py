class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        ans = 1
        max_ans = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                ans += 1
                max_ans = max(ans, max_ans)
            elif nums[i] == nums[i - 1]:
                continue
            else:
                ans = 1
        return max_ans
