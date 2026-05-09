class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        pre=1
        postfix=[]
        post=1
        answer=[]
        for i in range(len(nums)):
            prefix.append(pre)
            pre=pre*nums[i]

        for i in range(len(nums)-1,-1,-1):
            postfix.append(post)
            post=post*nums[i]
        postfix.reverse()
        for i in range(len(nums)):
            answer.append(prefix[i]*postfix[i])
        return answer