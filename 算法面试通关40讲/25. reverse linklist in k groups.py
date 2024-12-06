
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        gprev = dummy

        while True:
            kth = self.getKth(gprev, k)
            if kth == None:
                break
            gend = kth.next
            gstart = gprev.next
            prev = gprev.next
            curr = prev.next
            while curr != gend:
                curr.next, prev, curr = prev, curr, curr.next
            gstart.next, gprev.next, gprev = curr, prev, gstart
        return dummy.next

    def getKth(self, curr, k):
        while k > 0:
            if curr == None:
                return curr
            curr = curr.next
            k -= 1
        return curr

    # 递归解法
    def reverseKGroup_re(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return

        curr = head
        n = 1

        while curr.next:
            curr = curr.next
            n += 1

        if n < k:
            return head

        prev, curr = None, head
        for _ in range(k):
            curr.next, prev, curr = prev, curr, curr.next

        head.next = self.reverseKGroup(curr, k)

        return prev
