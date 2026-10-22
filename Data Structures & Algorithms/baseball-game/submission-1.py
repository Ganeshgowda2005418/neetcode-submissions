class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for ope in operations:
            if ope=="C":
                stack.pop()
            elif ope=="D":
                stack.append(2*stack[-1])
            elif ope=="+":
                stack.append(stack[-2]+stack[-1])
            else:
                stack.append(int(ope))
        return sum(stack)