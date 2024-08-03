# Definition for a Node.
from collections import defaultdict
from typing import Optional, List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            # i = ord(c) - ord("a")
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            # i = ord(c) - ord("a")
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            # i = ord(c) - ord("a")
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

if __name__ == '__main__':

    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple")) # return True
    print(trie.search("app")) # return False
    print(trie.startsWith("app")) # return True
    trie.insert("app")
    print(trie.search("app"))