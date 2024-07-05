# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next


if __name__ == '__main__':
    testLists = {
        1: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4],
        2: [ListNode(5), 1, 1],
    }

    for key in testLists:
        head = Solution().reverseBetween(testLists[key][0], testLists[key][1], testLists[key][2])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next