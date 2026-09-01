class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp=set()
        i=0
        for j in range(len(nums)):
            while abs(i-j)>k:
                mp.remove(nums[i])
                i+=1
            if nums[j] in mp :
                return True
            mp.add(nums[j])

        return False
    