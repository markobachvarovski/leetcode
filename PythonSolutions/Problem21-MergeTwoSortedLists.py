# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1

        return head.next

if __name__ == '__main__':
    testLists = {
        1: [[1,2,4], [1,3,4]],
        2: [[], []],
        3: [[], [0]],
    }

    for key in testLists:
        print(Solution().mergeTwoLists(testLists[key][0], testLists[key][1]))