# Definition for a Node.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

if __name__ == '__main__':
    testCases = {
        1: ListNode(0, ListNode(1, ListNode(2, ListNode(3)))),
    }

    for key in testCases:
        print(Solution().reverseList(testCases[key]))