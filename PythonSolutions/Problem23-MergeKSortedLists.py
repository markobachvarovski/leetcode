# Definition for a Node.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            midpoint = len(lists) // 2

            list1 = self.mergeKLists(lists[:midpoint])
            list2 = self.mergeKLists(lists[midpoint:])

            dummy = ListNode()
            curr = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next

            curr.next = list1 or list2

            return dummy.next

if __name__ == '__main__':
    testCases = {
        1: [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))],
        2: [],
        3: [None]
    }

    for key in testCases:
        head = Solution().mergeKLists(testCases[key])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next