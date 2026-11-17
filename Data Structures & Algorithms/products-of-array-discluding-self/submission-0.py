class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_0 = 0
        for num in nums:
            if num == 0:
                count_0 += 1
            else:
                product *= num
        if count_0 > 1:
            return [0] * len(nums)
        ans = []
        for num in nums:
            if num == 0:
                ans.append(product)
            elif count_0 == 1:
                ans.append(0)
            else:
                ans.append(int(product / num))
        return ans
