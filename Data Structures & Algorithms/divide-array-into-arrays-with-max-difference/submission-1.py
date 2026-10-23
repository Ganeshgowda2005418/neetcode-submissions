class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(0,len(nums),3):
            curr=nums[i:i+3]
            if curr[2]-curr[0]>k:
                return []
            res.append(curr)
        return res
