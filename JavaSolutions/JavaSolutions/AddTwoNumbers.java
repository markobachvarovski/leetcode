package JavaSolutions;

public class AddTwoNumbers {

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {

// Worst case runtime: O(n) where n is the number of nodes of the larger list

        ListNode answer = new ListNode(0, null);
        int remainder = 0;
        ListNode head = answer;

//        Loop until you reach the end of both lists
        while(!(l1 == null && l2 == null)) {
//            If l2 is longer than l1
            if(l1 == null) {

//                Can't simply connect l2 to answer, since there might be an unaccounted for remainder left over
//                What we need to do is loop over l2 until the remainder is 0, and at that point it's safe to set
//                answer.next = l2.next because we know we wouldn't have missed any leftover remainders
//                Consider the case l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9] to understand the purpose of this loop
                while (remainder != 0 || l2 == null) {

                    if (l2.val + remainder >= 10) {
                        answer.val = (l2.val + remainder) % 10;
                        remainder = 1;
                    }
                    else {
                        answer.val = l2.val + remainder;
                        remainder = 0;
                    }

//                    Checks ahead if the current node is the last one in l2 and adjusts answer accordingly
                    if (l2.next == null) {
//                        If the current node is the last, but we have a remainder, then the actual answer
//                        needs to have two more nodes to account for the remainder as well
                        if (remainder != 0) {
                            answer.next = new ListNode(0, null);
                            answer.next.val = remainder;
                            answer.next.next = null;
                            return head;
                        } else {
                            answer.next = null;
                            return head;
                        }

                    } else {
                        answer.next = new ListNode(0, null);
                    }

                    l2 = l2.next;
                    answer = answer.next;

                }

                if (remainder == 0) {
                    answer.val = l2.val + remainder;
                    answer.next = l2.next;
                }
                return head;

            } else if (l2 == null) {

                while (remainder != 0 || l1 == null) {

                    if (l1.val + remainder >= 10) {
                        answer.val = (l1.val + remainder) % 10;
                        remainder = 1;
                    }
                    else {
                        answer.val = l1.val + remainder;
                        remainder = 0;
                    }

                    if (l1.next == null) {
                        if (remainder != 0) {
                            answer.next = new ListNode(0, null);
                            answer.next.val = remainder;
                            answer.next.next = null;
                            return head;
                        } else {
                            answer.next = null;
                            return head;
                        }

                    } else {
                        answer.next = new ListNode(0, null);
                    }

                    l1 = l1.next;
                    answer = answer.next;

                }

                if (remainder == 0) {
                    answer.val = l1.val + remainder;
                    answer.next = l1.next;
                }
                return head;

            }  else {

                if (l1.val + l2.val + remainder >= 10) {
                    answer.val = (l1.val + l2.val + remainder) % 10;
                    remainder = 1;
                }
                else {
                    answer.val = l1.val + l2.val + remainder;
                    remainder = 0;
                }

                if (l1.next == null && l2.next == null){

                    if (remainder != 0) {
                        answer.next = new ListNode(0, null);
                        answer.next.val = remainder;
                        answer.next.next = null;

                        return head;
                    } else {
                        answer.next = null;
                        return head;
                    }
                } else {
                    answer.next = new ListNode(0, null);

                    l1 = l1.next;
                    l2 = l2.next;
                    answer = answer.next;
                }

            }
        }

        return head;
    }

    public static void main(String[] args) {
// Test case 1
//        ListNode l1 = new ListNode(2, new ListNode(4, new ListNode(3, null)));
//        ListNode l2 = new ListNode(5, new ListNode(6, new ListNode(4, null)));

// Test case 2
        ListNode l1 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, null)))))));
        ListNode l2 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, null))));

//Test case 3
//        ListNode l1 = new ListNode(0, null);
//        ListNode l2 = new ListNode(0, null);

        ListNode answer = addTwoNumbers(l1, l2);

        while (answer != null) {

            if (answer.next == null) {
                System.out.print(answer.val);
            } else {
                System.out.print(answer.val + " -> ");
            }

            answer = answer.next;
        }
    }
}
