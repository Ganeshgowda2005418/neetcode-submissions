class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxheight=0
        while l<r:
            currentheight=(r-l)*min(heights[l],heights[r])
            maxheight=max(currentheight,maxheight)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return maxheight

        