from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(comb, currSum, i):

            if currSum == target:
                res.append(comb[:])
                return
            if i >= len(candidates) or currSum > target:
                return

            comb.append(candidates[i])
            dfs(comb, currSum + candidates[i], i)

            comb.pop()
            dfs(comb, currSum, i+1)

        dfs([], 0, 0)
        return res


if __name__ == '__main__':
    testCases = {
        1: [[2,3,6,7], 7],
    }

    for key in testCases:
        print(f"{Solution().combinationSum(testCases[key][0], testCases[key][1])}")
