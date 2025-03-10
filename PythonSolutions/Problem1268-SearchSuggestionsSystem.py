from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.words = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        def add_word(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

                if len(node.words) < 3:
                    node.words.append(word)

            node.isWord = True

        products.sort()

        root = TrieNode()
        for product in products:
            add_word(root, product)

        ans = []
        node = root
        for char in searchWord:
            if char in node.children:
                node = node.children[char]
                ans.append(node.words)
            else:
                while len(ans) < len(searchWord):
                    ans.append([])
                break
        return ans

if __name__ == '__main__':
    testCases = {
        1: [["mobile","mouse","moneypot","monitor","mousepad"], "mouse"]
    }

    for key in testCases:
        print(Solution().suggestedProducts(testCases[key][0], testCases[key][1]))
