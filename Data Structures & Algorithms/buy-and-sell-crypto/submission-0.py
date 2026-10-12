class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        minprice = 1000000000000
        for i in range(len(prices)):
            if minprice >= prices[i]:
                minprice = prices[i]
            elif prices[i]-minprice >= profit:
                    profit = prices[i]-minprice
        return profit

