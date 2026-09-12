class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win=[]
        l=0
        for r in range(len(nums)):
            while (r-l+1)<=k:
                l+=1
            win.append(max(nums[l:r+1]))
        return win