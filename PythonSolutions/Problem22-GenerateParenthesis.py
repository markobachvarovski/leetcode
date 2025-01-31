from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(open_count, close_count, path):
            if open_count > n or close_count > n or open_count < close_count:
                return

            if open_count == n and close_count == n:
                ans.append(path)
                return
            backtrack(open_count + 1, close_count, path + '(')
            backtrack(open_count, close_count + 1, path + ')')

        backtrack(0, 0, '')
        return ans


if __name__ == '__main__':
    testCases = {
        1: [1],
        2: [2],
        3: [3]
    }

    for key in testCases:
        print(f"{Solution().generateParenthesis(testCases[key][0])}")
