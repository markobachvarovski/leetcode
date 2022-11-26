from typing import Optional


class ListNode:
    def __init__(self, x, nx):
        self.val = x
        self.next = nx


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Worst case runtime: O(n) where n is the number of nodes of the larger list

        answer = ListNode(None, None)
        remainder = 0
        head = answer


        # Loop until you reach the end of both lists
        while not (l1 is None and l2 is None):

            # If l2 is longer than l1
            if l1 is None:

                # Can't simply connect l2 to answer, since there might be an unaccounted for remainder left over
                # What we need to do is loop over l2 until the remainder is 0, and at that point it's safe to set
                # answer.next = l2.next because we know we wouldn't have missed any leftover remainders
                # Consider the case l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9] to understand the purpose of this loop
                while remainder != 0 or l2 is None:
                    if l2.val + remainder >= 10:
                        answer.val = (l2.val + remainder) % 10
                        remainder = 1
                    else:
                        answer.val = l2.val + remainder
                        remainder = 0

                    # Checks ahead if the current node is the last one in l2 and adjusts answer accordingly
                    if l2.next is None:
                        # If the current node is the last, but we have a remainder, then the actual answer
                        # needs to have two more nodes to account for the remainder as well
                        if remainder != 0:
                            answer.next = ListNode(None, None)
                            answer.next.val = remainder
                            answer.next.next = None

                            return head
                        else:
                            answer.next = None
                            return head
                    else:
                        answer.next = ListNode(None, None)

                    l2 = l2.next
                    answer = answer.next

                if remainder == 0:
                    answer.val = l2.val + remainder
                    answer.next = l2.next

                return head

            # Same logic as above applies
            elif l2 is None:
                while remainder != 0 or l1 is None:
                    if l1.val + remainder >= 10:
                        answer.val = (l1.val + remainder) % 10
                        remainder = 1
                    else:
                        answer.val = l1.val + remainder
                        remainder = 0

                    if l1.next is None:
                        if remainder != 0:
                            answer.next = ListNode(None, None)
                            answer.next.val = remainder
                            answer.next.next = None

                            return head
                        else:
                            answer.next = None
                            return head
                    else:
                        answer.next = ListNode(None, None)

                    l1 = l1.next
                    answer = answer.next

                if remainder == 0:
                    answer.val = l1.val + remainder
                    answer.next = l1.next

                return head

            # Same logic applies, except this time we're handling the values from both l1 and l2
            else:

                if l1.val + l2.val + remainder >= 10:
                    answer.val = (l1.val + l2.val + remainder) % 10
                    remainder = 1
                else:
                    answer.val = l1.val + l2.val + remainder
                    remainder = 0

                if l1.next is None and l2.next is None:
                    if remainder != 0:
                        answer.next = ListNode(None, None)
                        answer.next.val = remainder
                        answer.next.next = None

                        return head
                    else:
                        answer.next = None
                        return head
                else:
                    answer.next = ListNode(None, None)

                l1 = l1.next
                l2 = l2.next
                answer = answer.next

        return head


if __name__ == '__main__':
    # Test case 1
    # l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    # l2 = ListNode(5, ListNode(6, ListNode(4, None)))

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
