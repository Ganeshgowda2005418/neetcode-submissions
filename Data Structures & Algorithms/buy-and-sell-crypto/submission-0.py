class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        maxprice=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                currentprice=(prices[j]-prices[i])
                maxprice=max(currentprice,maxprice)
        return maxprice
        