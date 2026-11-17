class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return [list(x) for x in ans]
