class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        for i in range(len(tickets)):
            q.append(i)
        
        count=0
        while q:
            count+=1
            curr=q.popleft()
            tickets[curr]-=1
            if tickets[curr]==0:
                if curr==k:
                    return count
            else:
                q.append(curr)