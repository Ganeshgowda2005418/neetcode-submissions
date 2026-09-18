# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeset=set()
        curr=headA
        while curr:
            nodeset.add(curr)
            curr=curr.next
        curr=headB
        while curr:
            if curr in nodeset:
                return curr
            else:
                curr=curr.next
        return None