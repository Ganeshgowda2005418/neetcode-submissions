class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=defaultdict(set)
        count=0
        for i in range(len(nums)):
            if nums[i+1] in seen:
                count+=1
            else:
                count=0
        return count
        