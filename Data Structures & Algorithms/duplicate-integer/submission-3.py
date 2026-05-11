class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i in range(len(nums)):
            if i in hashset:
                return true
            hashset.add(i)
        return false