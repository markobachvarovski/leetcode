# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

if __name__ == '__main__':
    testLists = {
        1: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2],
        2: [ListNode(1), 1],
        3: [ListNode(1, ListNode(2)), 1],
    }

    for key in testLists:
        head = Solution().removeNthFromEnd(testLists[key][0], testLists[key][1])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next