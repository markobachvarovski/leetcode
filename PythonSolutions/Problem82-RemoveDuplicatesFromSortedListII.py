# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        curr = dummy

        while curr.next:
            if curr.next.next and curr.next.val == curr.next.next.val:
                val = curr.next.val
                while curr.next and curr.next.val == val:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

    # dummy = ListNode(0, head)
    #     prev = dummy
    #     prevUnique = dummy
    #
    #     curr = head
    #
    #     while curr.next is not None:
    #         if curr.val == curr.next.val:
    #             prevUnique = prev
    #         # elif curr.val == prev.val:
    #         #     prevUnique.next = curr.next
    #         else:
    #             if curr.val == prev.val:
    #                 prevUnique.next = curr.next
    #             else:
    #                 prevUnique = curr
    #
    #         prev = prev.next
    #         curr = curr.next
    #     return dummy.next


if __name__ == '__main__':
    testLists = {
        1: [ListNode(1,ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))],
        2: [ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))],

    }

    for key in testLists:
        head = Solution().deleteDuplicates(testLists[key][0])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next