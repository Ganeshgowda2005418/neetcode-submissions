class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            res=[]
            minheap=[]
            for n in arr:
                heapq.heappush(minheap,[abs(n-x),n])
            for _ in range(k):
                res.append(heapq.heappop(minheap)[1])
            res.sort()
            return res