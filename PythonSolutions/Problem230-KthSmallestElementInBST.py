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
        count = 0

        def inorderTraversal(node, k):
            nonlocal count

            if not node or count > k:
                return

            left = inorderTraversal(node.left, k)
            if left is not None:
                return left

            count += 1
            if count == k:
                return node.val

            return inorderTraversal(node.right, k)

            # return left or right

        return inorderTraversal(root, k)


if __name__ == '__main__':
    testCases = {
        1: [[3, 1, 4, None, 2], 1],
        2: [[5, 3, 6, 2, 4, None, None, 1], 3],
        3: [[100, 80, 120, 70, 90, 110, 130, 60, None, 85, 95, None, None, None, 140, None, None, None, None, 94, None, None, None], 6],
        4: [[31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9], 1]
    }

    for key in testCases:
        print(f"{Solution().kthSmallest(to_binary_tree(testCases[key][0]), testCases[key][1])}")