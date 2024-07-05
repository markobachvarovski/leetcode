# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        first, second, curr = head, head, head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        for _ in range(k % count):
            if first.next is None:
                first = head
            else:
                first = first.next

        while first.next:
            first = first.next
            second = second.next

        first.next = head
        head = second.next
        second.next = None

        return head


if __name__ == '__main__':
    testLists = {
        1: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2],
        2: [ListNode(0, ListNode(1, ListNode(2))), 4],
        3: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 123456],
    }

    for key in testLists:
        head = Solution().rotateRight(testLists[key][0], testLists[key][1])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next