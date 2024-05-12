class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        self.result = 0
        self.inorderTraversal(root, k)
        return self.result

    def inorderTraversal(self, node, k):
        if not node or self.count >= k:
            return

        self.inorderTraversal(node.left, k)

        self.count += 1
        if self.count == k:
            self.result = node.val
            return

        self.inorderTraversal(node.right, k)

if __name__ == '__main__':
    testCases = {
        1: [[3, 1, 4, None, 2], 1],
        2: [[5, 3, 6, 2, 4, None, None, 1], 3],
        3: [[100, 80, 120, 70, 90, 110, 130, 60, None, 85, 95, None, None, None, 140, None, None, None, None, 94, None, None, None], 6]
    }

    for key in testCases:
        print(f"{Solution().kthSmallest(to_binary_tree(testCases[key][0]), testCases[key][1])}")