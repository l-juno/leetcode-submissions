class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        front = 0
        end = 1
        if len(prices) <= 1:
            return 0
        
        while end < len(prices):
            currProfit = prices[end] - prices[front]
            print("currProfit: " + str(currProfit))
            maxProfit = max(maxProfit, currProfit)
            if prices[end] < prices[front]:
                front = end
            end += 1
        
        return maxProfit
            

        




        