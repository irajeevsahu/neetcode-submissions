class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            profit = max(prices[i] - buy_price, profit)
            buy_price = min(prices[i], buy_price)
        return profit
