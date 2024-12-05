from typing import Optional


class ListNode:
    def __init__(self, x, nx):
        self.val = x
        self.next = nx


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Worst case runtime: O(n) where n is the number of nodes of the larger list

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


if __name__ == '__main__':
    # Test case 1
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))

    # Test case 2
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

    # Test case 3
    # l1 = ListNode(0, None)
    # l2 = ListNode(0, None)

    ans = Solution().addTwoNumbers(l1, l2)

    while ans is not None:
        if ans.next is None:
            print(ans.val)
        else:
            print(ans.val, end=" -> ")
        ans = ans.next
