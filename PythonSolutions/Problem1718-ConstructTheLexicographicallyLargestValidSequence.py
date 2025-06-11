from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def dfs(pos):
            while pos < len(ans) and ans[pos] != 0:
                pos += 1

            if pos == len(ans):
                return True

            for num in range(n, 0, -1):
                if used[num]:
                    continue

                if num == 1:
                    ans[pos] = 1
                    used[1] = True

                    if dfs(pos + 1):
                        return True

                    ans[pos] = 0
                    used[1] = False
                else:
                    second_pos = pos + num
                    if second_pos < len(ans) and ans[second_pos] == 0:
                        ans[pos] = num
                        ans[second_pos] = num
                        used[num] = True

                        if dfs(pos + 1):
                            return True

                        ans[pos] = 0
                        ans[second_pos] = 0
                        used[num] = False

            return False

        dfs(0)
        return ans

if __name__ == '__main__':
    testCases = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7
    }

    for key in testCases:
        print(Solution().constructDistancedSequence(testCases[key]))
