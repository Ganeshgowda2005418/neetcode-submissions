class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num=sorted(nums)
        current=1
        longest=1
        for i in range(1,len(num)):
            if num[i]==num[i-1]:
                continue
            elif num[i]==num[i-1]+1:
                current+=1
            else:
                current=1
            longest=max(current,longest)
        return longest
