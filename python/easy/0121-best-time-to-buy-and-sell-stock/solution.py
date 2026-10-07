class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        bestProfit = 0
        profit = 0
        for i in prices:
            profit = i - lowest
            if profit > bestProfit:
                bestProfit = profit
            if i < lowest:
                lowest = i
            
        return bestProfit
            