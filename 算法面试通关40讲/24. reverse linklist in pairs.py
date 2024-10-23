# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0,head)
        pre = dummyhead

        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a 

        return dummyhead.next