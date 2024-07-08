# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = prev.next
        scout = prev.next

        for _ in range(k):
            if not scout:
                return dummy.next
            scout = scout.next

        while scout:
            for _ in range(k - 1):
                next_node = curr.next
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node

            for _ in range(k):
                prev = prev.next
                curr = prev.next

                if not scout:
                    return dummy.next
                scout = scout.next

        return dummy.next


if __name__ == '__main__':
    testLists = {
        1: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2],
        2: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3],
    }

    for key in testLists:
        head = Solution().reverseKGroup(testLists[key][0], testLists[key][1])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next