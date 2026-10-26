class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        Increasing,Decreasing=True,True
        for i in range(len(nums)-1):
            if not nums[i]<=nums[i+1]:
                Increasing=False
            if not nums[i]>=nums[i+1]:
                Decreasing=False
        return Increasing or Decreasing