class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap=[-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        q=deque()
        time=0
        while q or maxheap:
            time+=1
            if not maxheap:
                time=q[0][1]
                
            else:
                v=1+heapq.heappop(maxheap)
                if v:
                    q.append([v,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time