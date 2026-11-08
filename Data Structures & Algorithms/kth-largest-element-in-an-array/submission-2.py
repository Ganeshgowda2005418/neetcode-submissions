class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap=[]
        for n in nums:
            heapq.heappush(maxheap,-n)
        while k>1:
            heapq.heappop(maxheap)
            k-=1
        return -heapq.heappop(maxheap)