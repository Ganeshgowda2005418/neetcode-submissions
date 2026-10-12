class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minheap=[]
        for i,n in enumerate(nums):
            heapq.heappush(minheap,[n,i])
        print(minheap)
        l=0
        while l<k:
            n,i=heapq.heappop(minheap)
            val=n*multiplier
            heapq.heappush(minheap,[val,i])
            nums[i]=val
            l+=1
        return nums