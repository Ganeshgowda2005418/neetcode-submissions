class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for n in count.values():
            if n%2!=0:
                return False
        return True