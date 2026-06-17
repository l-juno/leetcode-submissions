class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for i in range(len(prices)):
            currProfit = prices[i] - lowest
            profit = max(profit, currProfit)
            lowest = min(lowest, prices[i])

        return profit
        