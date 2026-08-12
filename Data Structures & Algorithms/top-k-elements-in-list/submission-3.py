class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has=defaultdict(list)
        for i,num in enumerate (nums):
            has[nums[i]]=1+has.get(nums[i],0)
        return sorted(has, key=has.get, reverse=True)[:k]        