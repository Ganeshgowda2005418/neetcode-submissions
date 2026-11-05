class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []

        for i in range(len(prices) - 1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()

            original = prices[i]

            if stack:
                prices[i] -= stack[-1]

            stack.append(original)

        return prices