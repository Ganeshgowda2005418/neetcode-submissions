class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        for p in points:
            val=math.sqrt((0-p[0])**2+(0-p[1])**2)
            heapq.heappush(minheap,(val,p))
        l=[]
        for _ in range(k):
            val,p=heapq.heappop(minheap)
            l.append(p)
        return l