import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap=[-val for val in gifts]
        heapq.heapify(maxheap)
        for _ in range(k):
            val=-heapq.heappop(maxheap)
            val=math.isqrt(val)
            heapq.heappush(maxheap,-val)
        return -sum(maxheap)