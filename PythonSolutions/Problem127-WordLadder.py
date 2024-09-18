from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                adj_list[word[:i] + '_' + word[i + 1:]].append(word)

        visited = set()
        queue = deque([(beginWord, 1)])

        while queue:
            word, number_of_words = queue.popleft()
            if word in visited:
                continue

            if word == endWord:
                return number_of_words

            visited.add(word)
            for i in range(len(word)):
                neighbors = adj_list[word[:i] + '_' + word[i + 1:]]
                for neighbor in neighbors:
                    queue.append((neighbor, number_of_words + 1))

        return 0

if __name__ == '__main__':
    testCases = {
        1: [
            "hit",
            "cog",
            ["hot","dot","dog","lot","log","cog"]
        ],
        2: [
            "hit",
            "cog",
            ["hot","dot","dog","lot","log"]
        ]
    }

    for key in testCases:
        print(Solution().ladderLength(testCases[key][0], testCases[key][1], testCases[key][2]))