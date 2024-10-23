class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ch = head
        p = None
        q, r = None, None
        while ch:
            q = ch
            r = ch.next
            ch.next = p
            p = q
            ch = r

        return q

    def reverseList1(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev