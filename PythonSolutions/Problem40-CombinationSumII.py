from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(comb, currSum, i):
            if currSum == 0:
                res.append(comb[:])
                return
            if currSum <= 0:
                return

            prev = -1
            for i in range(i, len(candidates)):
                if candidates[i] == prev:
                    continue
                comb.append(candidates[i])
                dfs(comb, currSum - candidates[i], i + 1)
                comb.pop()
                prev = candidates[i]

        dfs([], target, 0)
        return res


if __name__ == '__main__':
    testCases = {
        1: [[10,1,2,7,6,1,5], 8],
        2: [[2,5,2,1,2], 5]
    }

    for key in testCases:
        print(f"{Solution().combinationSum(testCases[key][0], testCases[key][1])}")
