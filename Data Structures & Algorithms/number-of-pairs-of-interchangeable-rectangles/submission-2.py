class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count={}
        for w,h in rectangles:
            count[w/h]=count.get(w/h,0)+1
        res=0
        for c in count.values():
            if c>1:
                res+=c*(c-1)//2
        return res
