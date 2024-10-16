
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairMap = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in pairMap.values():
                stack.append(c)
            elif not stack or pairMap[c] != stack.pop():
                return False

        return len(stack) == 0

if __name__ == '__main__':
    testLists = {
        1: "()",
        2: "()[]{}",
        3: "(]",
        4: "([])",
        5: ""
    }

    for key in testLists:
        print(Solution().isValid(testLists[key]))