# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        cur = head
        while cur:
            if cur not in visited.keys():
                visited[cur] = True
                cur = cur.next
            else:
                return True
        return False

    def hasCycleI(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        fast, slow = head, head
        while fast != None and fast.next != None :
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


class Solution_II:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        visited = {}
        while cur is not None:
            if cur in visited.keys():
                return cur
            visited[cur] = True
            cur = cur.next