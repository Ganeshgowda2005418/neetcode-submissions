# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1_stack=[]
        l2_stack=[]
        while l1:
            l1_stack.append(l1.val)
            l1=l1.next
        while l2:
            l2_stack.append(l2.val)
            l2=l2.next
        prev=None
        carry=0
        total=0
        while l1_stack or l2_stack or carry:
            val1=l1_stack.pop() if l1_stack else 0
            val2=l2_stack.pop() if l2_stack else 0
            total=val1+val2+carry
            Node=ListNode(total%10)
            carry=total//10
            Node.next=prev
            prev=Node
        return prev