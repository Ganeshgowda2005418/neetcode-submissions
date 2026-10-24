class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res=0
        for i in range(len(nums)):
            currmax=nums[i]
            currmin=nums[i]
            for j in range(i,len(nums)):
                currmax=max(currmax,nums[j])
                currmin=min(currmin,nums[j])
                if currmax-currmin<=limit:
                    res=max(res,j-i+1)
                else:
                    break
            
        return res