class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            total=0
            while n>0:
                digits=n%10
                total+=digits*digits
                n=n//10
            return total
        seen=set()
        while True:
            s=happy(n)
            if s==1:
                return True
            elif s in seen:
                return False
            else:
                seen.add(s)
                n=s