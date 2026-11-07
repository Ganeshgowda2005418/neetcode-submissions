class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[]
        for i,n in count.items():
            if n>1:
                res.append(i)
        return res
