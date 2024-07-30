# Definition for a Node.
from collections import defaultdict
from typing import Optional, List


class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

if __name__ == '__main__':
    # testCases = {
    #     1: [TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))],
    #     2: [TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))],
    #     3: [TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(5)))],
    # }

    # for key in testCases:
    #     print(Solution().zigzagLevelOrder(testCases[key][0]))

    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple")) # return True
    print(trie.search("app")) # return False
    print(trie.startsWith("app")) # return True
    trie.insert("app")
    print(trie.search("app"))