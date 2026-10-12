class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf') 
        for price in prices:
            if minprice >= price:
                minprice = price
            elif (price - minprice) > profit:
                profit = price - minprice
        return profit

