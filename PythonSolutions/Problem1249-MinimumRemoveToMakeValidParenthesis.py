class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        to_remove.update(stack)
        result = [char for i, char in enumerate(s) if i not in to_remove]

        return ''.join(result)


if __name__ == '__main__':
    testCases = {
        1: "lee(t(c)o)de)",
        2: "a)b(c)d",
        3: "))((",
    }

    for key in testCases:
        print(Solution().minRemoveToMakeValid(testCases[key]))
