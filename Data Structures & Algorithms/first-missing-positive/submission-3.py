class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=set(nums)
     
        i=1
        while True:
            if i not in n:
                return i
            i+=1