class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        res=[0,0]
        for i in range(1,len(nums)+1):
            if count[i]==0:
                res[1]=i
            if count[i]==2:
                res[0]=i
        return res