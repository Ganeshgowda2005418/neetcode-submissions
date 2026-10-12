class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap=[-val for val in gifts]
        heapq.heapify(maxheap)
        for _ in range(k):
            val=-heapq.heappop(maxheap)
            heapq.heappush(maxheap,-floor(sqrt(val)))
        return -sum(maxheap)