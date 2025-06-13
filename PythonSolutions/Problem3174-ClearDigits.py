class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isdigit() and stack:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

if __name__ == '__main__':
    testCases = {
        1: "abc",
        2: "cb34"
    }

    for key in testCases:
        print(Solution().clearDigits(testCases[key]))
