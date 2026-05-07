class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        for n in nums:
            count[n]=1+count.get(n,0)
        sorted_list =sorted(count.items(), key=lambda x: x[1], reverse=True)
        res=[]
        for num, freq in sorted_list[:k]:
            res.append(num)
        return res
        


  
        