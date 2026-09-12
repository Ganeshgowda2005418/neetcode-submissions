class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=sorted(nums)
        count=0
        for i in n:
            if i+1 in n:
                count+=1
        return count