from _heapq import heapify
class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count=Counter(arr)
       
        minheap=[]
        heapq.heapify(minheap)
        for cnt in count.values():
            heapq.heappush(minheap,cnt)
        while minheap and k >= minheap[0]:
            k-=heapq.heappop(minheap)
            
        return len(minheap)