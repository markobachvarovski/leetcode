# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head

        head_smaller = ListNode(-500)
        head_greater = ListNode(-500)

        curr_smaller = head_smaller
        curr_greater = head_greater

        while curr:
            if curr.val < x:
                curr_smaller.next = curr
                curr_smaller = curr
            else:
                curr_greater.next = curr
                curr_greater = curr

            curr = curr.next

        curr_greater.next = None
        curr_smaller.next = head_greater.next

        return head_smaller.next

if __name__ == '__main__':
    testLists = {
        1: [ListNode(1,ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3],
        2: [ListNode(2, ListNode(1)), 2],
    }

    for key in testLists:
        head = Solution().partition(testLists[key][0], testLists[key][1])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next