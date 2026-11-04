class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = len(nums) - 1

            k = i + 1
            while k < l:
                curr_s = nums[i] + nums[k] + nums[l]
                if curr_s == 0:
                    res.append([nums[i], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif curr_s < 0:
                    k += 1
                else:
                    l -= 1
        return res
