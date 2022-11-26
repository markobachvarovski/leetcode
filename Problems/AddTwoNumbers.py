from typing import Optional


class ListNode:
    def __init__(self, x, nx):
        self.val = x
        self.next = nx


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        answer = ListNode(None, None)
        remainder = 0
        head = answer

        while not (l1 is None and l2 is None):

            if l1 is None:
                while remainder != 0 or l2 is None:
                    if l2.val + remainder >= 10:
                        answer.val = (l2.val + remainder) % 10
                        remainder = 1
                    else:
                        answer.val = l2.val + remainder
                        remainder = 0

                    if l2.next is None:
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
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))

    # l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(8, ListNode(9, ListNode(9, None)))))))
    # l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
    #
    # l1 = ListNode(0, None)
    # l2 = ListNode(0, None)

    ans = Solution().addTwoNumbers(l1, l2)
    print("Hi")
