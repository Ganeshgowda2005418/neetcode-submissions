class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprice=0
        for price in prices:
            minprice=min(price,minprice)
            profit=price-minprice
            maxprice=max(profit,maxprice)
        return maxprice