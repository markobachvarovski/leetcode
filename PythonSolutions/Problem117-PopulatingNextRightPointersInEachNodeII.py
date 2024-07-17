# Definition for a Node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root

class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        curr = root
        dummy = TreeNode(-999)
        head = root

        while head:

            curr = head  # initialize current level's head
            prev = dummy  # init prev for next level linked list traversal
            # iterate through the linked-list of the current level and connect all the siblings in the next level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            head = dummy.next  # update head to the linked list of next level
            dummy.next = None  # reset dummy node

        return root

COUNT = [10]
def print2DUtil(root, space):
    if root is None:
        return

    space += COUNT[0]

    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    print2DUtil(root.left, space)


def print2D(root):
    print2DUtil(root, 0)

if __name__ == '__main__':
    testCases = {
        1: [TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))],
    }

    for key in testCases:
        print(f"{print2D(Solution().connect(testCases[key][0]))}")
        print("\n------------------------------------------------------------------------\n")