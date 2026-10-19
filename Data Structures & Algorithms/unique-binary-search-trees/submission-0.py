class Solution:
    def numTrees(self, n: int) -> int:
        counts = [0] * (n + 1)
        counts[0] = 1
        for size in range(1,n+1):
            for left in range(size): counts[size] += counts[left] * counts[size-1-left]
        return counts[n]
