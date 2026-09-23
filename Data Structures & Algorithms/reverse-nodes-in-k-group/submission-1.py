class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevnode = dummy

        while True:
            kth = self.kthnode(prevnode, k)

            if not kth:
                break

            groupNext = kth.next

            prev = groupNext
            curr = prevnode.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevnode.next
            prevnode.next = kth
            prevnode = tmp

        return dummy.next

    def kthnode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr
