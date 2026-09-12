class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        while l<=r:
            mid=l+(r-l)//2
            if mid<len(nums) and target==nums[mid]:
                return mid
            if mid<len(nums) and nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return mid