class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-x for x in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap)>1:
            curr=(-heapq.heappop(maxHeap))-(-heapq.heappop(maxHeap))
            if curr:
                heapq.heappush(maxHeap,-curr)
        return -heapq.heappop(maxHeap) if maxHeap else 0