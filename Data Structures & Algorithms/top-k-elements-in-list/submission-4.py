class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        minheap=[]
        for i,n in count.items():
           heapq.heappush(minheap,[-n,-i])
        res=[]
       
        for _ in range(k):
            res.append(-(heapq.heappop(minheap))[1])
            print(res)
        return res