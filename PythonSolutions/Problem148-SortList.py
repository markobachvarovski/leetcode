# Definition for a Node.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        smallerHead = self.sortList(head)
        biggerHead = self.sortList(mid)

        dummy = ListNode()
        curr = dummy
        while smallerHead and biggerHead:
            if smallerHead.val < biggerHead.val:
                curr.next = smallerHead
                smallerHead = smallerHead.next
            else:
                curr.next = biggerHead
                biggerHead = biggerHead.next
            curr = curr.next

        curr.next = smallerHead or biggerHead

        return dummy.next

if __name__ == '__main__':
    testCases = {
        1: ListNode(4, ListNode(2, ListNode(1, ListNode(3)))),
        2: ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    }

    for key in testCases:
        head = Solution().sortList(testCases[key])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next