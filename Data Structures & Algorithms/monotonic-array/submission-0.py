class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def increasing(n):
            for i in range(len(n)-1):
                if n[i]<n[i+1]:
                    return False
            return True
        def decreasing(n):
            for i in range(len(n)-1):
                if n[i]>n[i+1]:
                    return False
            return True
        i=0
        if nums[i]>nums[i+1]:
            res=increasing(nums)
        else:
            res=decreasing(nums)
        return res